#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    sys.exit()


deps = [
    'gevent>=0.13.6',
    'greenlet>=0.3.1',
    'gunicorn>=0.13.4',
    'static>=0.4'
]

setup(
    name='goldenarch',
    version='0.0.4',
    install_requires=deps,
    description='Serves crap. faast.',
    long_description='Meh.',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='http://kennethreitz.com',
    packages=['goldenarch'],
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
        # 'Programming Language :: Python :: 3.2',
    ),
    entry_points={
        'console_scripts': [
            'goldenarch = goldenarch:cli',
        ],
    }
)
