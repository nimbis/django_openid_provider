============
Requirements
============

The Python OpenID library is required to run ``openid_provider``. By default
it'll use ``openid.store.filestore.FileOpenIDStore`` for persistent storage
of OpenID related data.

To change the file system location that the default storage uses, you can
optionally provide a ``OPENID_PROVIDER_FILESTORE_PATH`` setting.

In case you don't want to store the OpenID related data on a file system,
it's also possible to make use of the ``DjangoOpenIDStore`` contained in
the django_openid_auth_ app. Simply add an ``OPENID_PROVIDER_STORE`` setting
to your settings::

    OPENID_PROVIDER_STORE = 'django_openid_auth.store.DjangoOpenIDStore'

This is especially useful in case your site is deployed in shared hosting
environments.

.. _django_openid_auth: https://launchpad.net/django-openid-auth


==================
Basic Installation
==================

1. Copy/install ``openid_provider`` into your project directory (or link to it).
2. Add ``'openid_provider'`` to ``INSTALLED_APPS`` and its dependencies::

    INSTALLED_APPS = (
        # ...
        'django.contrib.auth',
        'django.contrib.sessions',
        'openid_provider',
        # ...
    )

3. Add ``openid_provider/urls.py`` to your urlpatterns, e.g.::

    urlpatterns = patterns('',
        # ...
        url(r'^openid/', include('openid_provider.urls')),
        # ...
    )

4. Run::

    python manage.py syncdb

   to create required tables to your database.


====================
What is not provided
====================

This application does not include most basic template every django project
should have: ``base.html``. You should have ``base.html`` file in one of your
`settings.TEMPLATE_DIRS`_ directories and it should contain 3 base blocks:

  - title
  - extrahead
  - content

(see DosAndDontsForApplicationWriters_ and `django template inheritance`_)

.. _`settings.TEMPLATE_DIRS`:
   http://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
.. _DosAndDontsForApplicationWriters:
   http://code.djangoproject.com/wiki/DosAndDontsForApplicationWriters
.. _`django template inheritance`:
   http://docs.djangoproject.com/en/dev/topics/templates/#id1

If your base template is named differently you should override
``openid_provider/base.html`` to contain something like::

    {% extends "your_base_template_name.html" %}

If your base template have different blocks you could easily remap those::

    {% block your_content_block_name %}{% block content %}{% endblock %}{% endblock %}

