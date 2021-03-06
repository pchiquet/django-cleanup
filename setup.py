#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2012 Ilya Shalyapin
#
#  django-cleanup is free software under terms of the MIT License.
#

import os
import re
from codecs import open as codecs_open
from setuptools import setup, find_packages


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs_open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''', version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError('Unable to find version string.')


setup(
    name     = 'django-cleanup',
    version  = find_version('django_cleanup', '__init__.py'),
    packages = ['django_cleanup'],
    include_package_data=True,
    requires = ['python (>= 2.7)', 'django (>= 1.6)'],
    description  = 'Deletes old files.',
    long_description = read('README.rst'),
    author       = 'Ilya Shalyapin',
    author_email = 'ishalyapin@gmail.com',
    url          = 'https://github.com/un1t/django-cleanup',
    download_url = 'https://github.com/un1t/django-cleanup/tarball/master',
    license      = 'MIT License',
    keywords     = 'django',
    classifiers  = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
