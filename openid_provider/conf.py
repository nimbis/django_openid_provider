import os
from django.conf import settings

STORE = getattr(settings, 'OPENID_PROVIDER_STORE',
                'openid.store.filestore.FileOpenIDStore')

if STORE == 'openid.store.filestore.FileOpenIDStore':
    import tempfile
    tempdir = tempfile.gettempdir()
    
    FILESTORE_PATH = getattr(settings, 'OPENID_PROVIDER_FILESTORE_PATH',
                             os.path.join(tempdir, 'openid-filestore'))

SREG_DATA_CALLBACK = getattr(settings, 'OPENID_PROVIDER_SREG_DATA_CALLBACK',
                             'openid_provider.utils.get_default_sreg_data')

AX_DATA_CALLBACK = getattr(settings, 'OPENID_PROVIDER_AX_DATA_CALLBACK',
                           'openid_provider.utils.get_default_ax_data')

AX_EXTENSION = getattr(settings, 'OPENID_PROVIDER_AX_EXTENSION', False)

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# RPs without relying party verification mechanisms will be each time
# redirected to decide page, set to True to disable this:
FAILED_DISCOVERY_AS_VALID = getattr(
    settings, 'OPENID_FAILED_DISCOVERY_AS_VALID', False)
