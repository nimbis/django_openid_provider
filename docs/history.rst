=======
History
=======

v0.6
----
Released 2014-03-31.

* When pressing "No" on decide page authentication is now cancelled as it
  supposed to be, fixes :issue:`6`.
* Added South migrations

  .. warning:: you must fake initial migration if you already have
     working openid_provider installation.
* Django 1.6 compatibility (use openid toPostArgs/decodeRequest internal
  serializer).

v0.5
----
Released 2013-12-23.

* Security enchancement:
  `OpenID Authentication 2.0 9.2.1 <http://openid.net/specs/openid-authentication-2_0.html#rfc.section.9.2.1>`_
  was implemented, fixes :issue:`4`.
* Fixed landing page view to handle redirect URL GET params correctly.
* Added OPENID_PROVIDER_SREG_DATA_CALLBACK setting for custom SREG callback
  functions.
* Added AX support, new OPENID_PROVIDER_AX_DATA_CALLBACK callback.
* Added Django 1.5 support.
* Added Django 1.5 custom user model support.
* Fixed response page javascript to submit the correct form when there is more than one.

v0.4
----
Released 2010-12-30.

* CSRF enabled sites support (thx to Jannis).
* SREG support (thx to Jannis).

v0.3
----
Released 2010-06-08.

* Better Djangos DosAndDontsForApplicationWriters compliance.
* Added MANIFEST.in and setup.py (thx Bruno).

v0.2
----
Released 2010-02-03.

* Better support for multiple identities - you can select one as default (if none identity is claimed in request).
* Added checking of claimed identity ownership.
* Added documentation.

v0.1
----
Released 2009-11-23.

* Initial version.


=======
Credits
=======

Django OpenID Provider is developed by Roman Barczyński based on code from:

- simon (`django code snippets <http://www.djangosnippets.org/snippets/310/>`_)
- python-openid-2.2.4 examples/djopenid


Contributors
------------

`Bruno Renié`_

* initial setup.py and MANIFEST.in

`Jannis Leidel`_

* code cleanup (tab2spaces, PEP8),
* sreg support,
* CSRF exempt for openid_server,
* simplified host resolution,
* ability to specify OPENID_PROVIDER_STORE in settings.

.. _`Bruno Renié`: http://bitbucket.org/bruno
.. _`Jannis Leidel`: http://bitbucket.org/jezdez
