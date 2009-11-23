# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 : */

from django.conf.urls.defaults import *

urlpatterns = patterns('openid_provider.views',
	url(r'^$', 'openid_server', name='openid-provider-root'),
	url(r'^id/(.*)/$', 'openid_identity', name='openid-provider-identity'),
	url(r'^decide/$', 'openid_decide', name='openid-provider-decide'),
	url(r'^xrds/$', 'openid_xrds', name='openid-provider-xrds'),
)
