== Basic Installation ==

 1. Copy openid_provider into your project directory.

 2. Add 'openid_provider' to INSTALLED_APPS,
    openid_provider requre at least:
    django.contrib.auth and django.contrib.sessions

 3. Add openid_provider/urls.py to your urlpatterns, e.g.:
    urlpatterns = patterns('',
	  ...
	  url(r'^openid/', include('openid_provider.urls')),
	  ...
	)

 4. Run python manage.py syncdb to create required tables
    to your database.


== Features ==

  1. Automatic redirect to login page for unauthorized users.

  2. Semi-automated creation of OpenID identifiers (leave OpenID field empty).

  3. Decision page for adding trust_root to one's OpenID trusted sites.

