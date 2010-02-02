# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 fdm=indent : */
# some code from http://www.djangosnippets.org/snippets/310/ by simon
# and from examples/djopenid from python-openid-2.2.4

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

from models import *
from openid.server.server import Server

import datetime

def get_base_uri(req):
	name = req.META['HTTP_HOST']
	try: name = name[:name.index(':')]
	except: pass

	try: port = int(req.META['SERVER_PORT'])
	except: port = 80

	proto = req.META['SERVER_PROTOCOL']
	if 'HTTPS' in proto:
		proto = 'https'
	else:
		proto = 'http'
	
	if port in [80, 443] or not port:
		port = ''
	else:
		port = ':%s' % port
	
	return '%s://%s%s' % (proto, name, port)

def django_response(webresponse):
	"Convert a webresponse from the OpenID library in to a Django HttpResponse"
	response = HttpResponse(webresponse.body)
	response.status_code = webresponse.code
	for key, value in webresponse.headers.items():
		response[key] = value
	return response

def openid_server(req):
	"""
	This view is the actual OpenID server - running at the URL pointed to by 
	the <link rel="openid.server"> tag. 
	"""
	host = get_base_uri(req)
	try:
		# if we have django_openid_auth in applications directory
		# then we can use DjangoOpenIDStore
		from django_openid_auth.store import DjangoOpenIDStore
		store = DjangoOpenIDStore()
	except:
		# otherwise use FileOpenIDStore
		OPENID_FILESTORE = '/tmp/openid-filestore'
		from openid.store.filestore import FileOpenIDStore
		store = FileOpenIDStore(OPENID_FILESTORE)
		
	server = Server(store, op_endpoint="%s%s" % (host, reverse('openid-provider-root')))

	# Clear AuthorizationInfo session var, if it is set
	if req.session.get('AuthorizationInfo', None):
		del req.session['AuthorizationInfo']

	querydict = dict(req.REQUEST.items())
	orequest = server.decodeRequest(querydict)
	if not orequest:
		orequest = req.session.get('OPENID_REQUEST', None)
		if not orequest:
			# not request, render info page:
			return render_to_response('openid_provider/server.html',
				{'host': host,},
				context_instance=RequestContext(req))
		else:
			# remove session stored data:
			del req.session['OPENID_REQUEST']

	if orequest.mode in ("checkid_immediate", "checkid_setup"):

		if not req.user.is_authenticated():
			return landing_page(req, orequest)

		openid = openid_is_authorized(req, orequest.identity, orequest.trust_root)

		if openid is not None:
			oresponse = orequest.answer(True, identity="%s%s" % (
				host, reverse('openid-provider-identity', args=[openid.openid])))
		elif orequest.immediate:
			raise Exception('checkid_immediate mode not supported')
		else:
			req.session['OPENID_REQUEST'] = orequest
			return HttpResponseRedirect(reverse('openid-provider-decide'))
	else:
		oresponse = server.handleRequest(orequest)
	webresponse = server.encodeResponse(oresponse)
	return django_response(webresponse)

def openid_xrds(req, identity=False, id=None):
	from openid.yadis.constants import YADIS_CONTENT_TYPE
	from openid.consumer.discover import OPENID_IDP_2_0_TYPE, OPENID_2_0_TYPE

	if identity:
		types = [OPENID_2_0_TYPE]
	else:
		types = [OPENID_IDP_2_0_TYPE]

	response = render_to_response('openid_provider/xrds.xml',
			{
				'host': get_base_uri(req),
				'types': types,
				'endpoints': [reverse('openid-provider-root')]
			},
			context_instance=RequestContext(req))
	response['Content-Type'] = YADIS_CONTENT_TYPE
	return response

def openid_decide(req):
	"""
	The page that asks the user if they really want to sign in to the site, and
	lets them add the consumer to their trusted whitelist.
	# If user is logged in, ask if they want to trust this trust_root
	# If they are NOT logged in, show the landing page
	"""
	from openid.server.trustroot import verifyReturnTo
	from openid.yadis.discover import DiscoveryFailure
	from openid.fetchers import HTTPFetchingError

	orequest = req.session.get('OPENID_REQUEST')

	if not req.user.is_authenticated():
		return landing_page(req, orequest)
	try:
		openid = req.user.openid_set.all()[0]
	except IndexError, ObjectDoesNotExist:
		return error_page(req, "You are signed in but you don't have OpenID here!")

	if req.method == 'POST' and req.POST.get('decide_page', False):
		allowed = 'allow' in req.POST
		openid.trustedroot_set.create(trust_root=orequest.trust_root)
		return HttpResponseRedirect(reverse('openid-provider-root'))

	# verify return_to of trust_root
	try:
		trust_root_valid = verifyReturnTo(orequest.trust_root, orequest.return_to ) and "Valid" or "Invalid"
	except HTTPFetchingError:
		trust_root_valid = "Unreachable"
	except DiscoveryFailure:
		trust_root_valid = "DISCOVERY_FAILED"

	return render_to_response('openid_provider/decide.html', {
			'title': 'Trust this site?',
			'trust_root': orequest.trust_root,
			'trust_root_valid': trust_root_valid,
			'identity': orequest.identity,
		},
		context_instance=RequestContext(req))

def error_page(req, msg):
	return render_to_response('error.html', {
		'title': 'Error',
		'msg': msg,
		},
		context_instance=RequestContext(req))

def landing_page(req, orequest):
	"""
	The page shown when the user attempts to sign in somewhere using OpenID 
	but is not authenticated with the site. For idproxy.net, a message telling
	them to log in manually is displayed.
	"""
	from django.contrib.auth import REDIRECT_FIELD_NAME
	from django.conf import settings

	req.session['OPENID_REQUEST'] = orequest
	login_url = settings.LOGIN_URL
	path = req.get_full_path()

	return HttpResponseRedirect('%s?%s=%s' % (
		login_url, REDIRECT_FIELD_NAME, path
		))

import urlparse
def openid_is_authorized(req, identity_url, trust_root):
	"""
	Check that they own the given identity URL, and that the trust_root is 
	in their whitelist of trusted sites.
	"""
	if not req.user.is_authenticated():
		return None

	try:
		openid = req.user.openid_set.all()[0]
	except IndexError, ObjectDoesNotExist:
		return None

	if openid.trustedroot_set.filter(trust_root=trust_root).count() < 1:
		return None

	return openid
