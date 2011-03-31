# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 fdm=indent : */
# some code from http://www.djangosnippets.org/snippets/310/ by simon
# and from examples/djopenid from python-openid-2.2.4
from openid_provider import conf
from openid.extensions import ax, sreg

from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

def import_module_attr(path):
    package, module = path.rsplit('.', 1)
    return getattr(import_module(package), module)

def get_default_sreg_data(request, orequest):
    return {
        'email': request.user.email,
        'nickname': request.user.username,
        'fullname': request.user.get_full_name(),
    }

def get_default_ax_data(request, orequest):
    return {
        'http://axschema.org/contact/email': request.user.email,
        'http://axschema.org/namePerson': request.user.get_full_name(),
        'http://axschema.org/namePerson/friendly': request.user.username,
        'http://axschema.org/namePerson/first': request.user.first_name,
        'http://axschema.org/namePerson/last': request.user.last_name,
    }

def add_sreg_data(request, orequest, oresponse):
    callback = get_sreg_callback()
    if callback is None or not callable(callback):
        return
    sreg_data = callback(request, orequest)
    sreg_req = sreg.SRegRequest.fromOpenIDRequest(orequest)
    sreg_resp = sreg.SRegResponse.extractResponse(sreg_req, sreg_data)
    oresponse.addExtension(sreg_resp)

def add_ax_data(request, orequest, oresponse):
    callback = get_ax_callback()
    if callback is None or not callable(callback):
        return
    ax_data = callback(request, orequest)
    ax_req = ax.FetchRequest.fromOpenIDRequest(orequest)
    ax_resp = ax.FetchResponse(ax_req)
    if ax_req is not None:
        for attr in ax_req.getRequiredAttrs():
            value = ax_data.get(attr, None)
            if value is not None:
                ax_resp.addValue(attr, value)
    oresponse.addExtension(ax_resp)

def get_sreg_callback():
    try:
        return import_module_attr(conf.SREG_DATA_CALLBACK)
    except (ImportError, AttributeError):
        return None

def get_ax_callback():
    try:
        return import_module_attr(conf.AX_DATA_CALLBACK)
    except (ImportError, AttributeError):
        return None

def get_store(request):
    try:
        store_class = import_module_attr(conf.STORE)
    except ImportError:
        raise ImproperlyConfigured("OpenID store %r could not be imported" % conf.STORE)
    # The FileOpenIDStore requires a path to save the user files.
    if conf.STORE == 'openid.store.filestore.FileOpenIDStore':
        return store_class(conf.FILESTORE_PATH)
    return store_class()
