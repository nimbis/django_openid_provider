== Basic Installation ==

1. Copy openid_provider into your project directory.

2. Add 'openid_provider' to INSTALLED_APPS,
    openid_provider requre at least:
{{{
#!python
'django.contrib.auth',
'django.contrib.sessions',
'openid_provider',
}}}

3. Add openid_provider/urls.py to your urlpatterns, e.g.:
{{{
#!python
urlpatterns = patterns('',
    ...
    url(r'^openid/', include('openid_provider.urls')),
    ...
)
}}}

4. Run 
{{{
#!python
python manage.py syncdb
}}}
 to create required tables to your database.

== Features ==

* Automatic redirect to login page for unauthorized users.
* Semi-automated creation of OpenID identifiers (leave OpenID field empty).
* Decision page for adding trust_root to one's OpenID trusted sites.

