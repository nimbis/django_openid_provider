# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = "django_openid_provider",
    version = "0.4",
    author = "Roman Barczyński",
    description = "An OpenID provider for your django.contrib.auth accounts",
    long_description = open("README.txt").read(),
    license = "Apache",
    url = "http://www.romke.net/django/openid_provider/",
    download_url = "https://bitbucket.org/romke/django_openid_provider",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
