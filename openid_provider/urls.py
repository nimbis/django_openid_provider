# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 : */

try:
    from django.conf.urls import patterns, url
except ImportError:  # Django < 1.4
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('openid_provider.views',
    url(r'^$', 'openid_server', name='openid-provider-root'),
    url(r'^decide/$', 'openid_decide', name='openid-provider-decide'),
    url(r'^xrds/$', 'openid_xrds', name='openid-provider-xrds'),
    url(r'^(?P<id>.*)/$', 'openid_xrds', {'identity': True}, name='openid-provider-identity'),
)
