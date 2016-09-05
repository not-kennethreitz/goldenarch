# -*- coding: utf-8 -*-

"""
goldenarch.py
~~~~~~~~~~~~~

Serves crap. Fast.
"""
from __future__ import print_function

import os
import subprocess

import static

PORT = os.environ.get('PORT', 8000)
STATIC_DIR = os.environ.get('STATIC_DIR', '.')


app = static.Cling(STATIC_DIR)

def cli():
    print('Serving crap. Fast.')

    cmd = (
        'gunicorn goldenarch:app '
        '-b "0.0.0.0:{port}" '
        '-w 16 -k gevent -t 2 '
        '--name goldenarch'
    ).format(port=PORT)

    return subprocess.call(cmd)


if __name__ == '__main__':
    cli()