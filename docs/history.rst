=======
History
=======

tip
---

* Fixed landing page view to handle redirect URL GET params correctly.
* Added setting OPENID_SREG_DATA_CALLBACK setting for custom SREG callback
  functions.
* Added AX support, new OPENID_AX_DATA_CALLBACK callback.

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

- simon (`django code snippets`_)
- python-openid-2.2.4 examples/djopenid

.. _`django code snippets`: http://www.djangosnippets.org/snippets/310/


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
