#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The setup script for audit_tools
"""

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Grab package info from __about__  so we aren't storing it in two places.
# See: https://packaging.python.org/guides/single-sourcing-package-version/
about = {}
with open(os.path.join(here, 'audit_tools', '__about__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # This should only be the packages this project actually requires to work
    # Don't include packages needed for development (those go in Pipfile).
    # TODO: put package requirements here
]

test_requirements = [
    'pytest',
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme + '\n\n' + history,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    platforms=about['__platforms__'],
    packages=find_packages(include=['audit_tools']),
    package_dir={'audit_tools':
                 'audit_tools'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements
)
