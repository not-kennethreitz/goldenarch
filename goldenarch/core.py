# -*- coding: utf-8 -*-

"""
goldenarch.py
~~~~~~~~~~~~~

Serves crap. Fast.
"""

import os
import sys

import static

PORT = os.environ.get('PORT', 8000)

def app(static_dir):
    return static.Cling(static_dir)

def cli():
    print 'Serving crap. Fast.'

    static_dir = sys.argv[1]

    argv = [
        'gunicorn', 'goldenarch:app("{dir}")'.format(dir=static_dir),
        '-b', '0.0.0.0:{port}'.format(port=PORT),
        '-w', '16', '-k', 'gevent', '-t', '2',
        '--name', 'goldenarch'
    ]

    os.execvp('gunicorn', argv)


if __name__ == '__main__':
    cli()
