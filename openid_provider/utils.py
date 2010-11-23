# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 fdm=indent : */
# some code from http://www.djangosnippets.org/snippets/310/ by simon
# and from examples/djopenid from python-openid-2.2.4

from openid.extensions import sreg

def get_base_uri(request):
    name = request.META['HTTP_HOST']
    try:
        name = name[:name.index(':')]
    except IndexError:
        pass
    try:
        port = int(request.META['SERVER_PORT'])
    except ValueError:
        port = 80
    if request.is_secure():
        proto = 'https'
    else:
        proto = 'http'
    if port in [80, 443] or not port:
        port = ''
    else:
        port = ':%s' % port
    return '%s://%s%s' % (proto, name, port)

def add_sreg_data(request, orequest, oresponse):
    sreg_req = sreg.SRegRequest.fromOpenIDRequest(orequest)
    sreg_resp = sreg.SRegResponse.extractResponse(sreg_req, {
        'email': request.user.email,
        'nickname': request.user.username,
        'fullname': request.user.get_full_name(),
    })
    oresponse.addExtension(sreg_resp)
