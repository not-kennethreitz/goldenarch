# -*- coding: utf-8 -*-

"""
goldenarch.py
~~~~~~~~~~~~~

Serves crap. Fast.
"""

import os

from werkzeug.wrappers import Request
from werkzeug.wsgi import SharedDataMiddleware


PORT = os.environ.get('PORT', 8000)
STATIC_DIR = os.environ.get('STATIC_DIR', '.')

class GoldenArch(object):
    def __init__(self):
        super(GoldenArch, self).__init__()

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def cli():
    print 'Serving crap. Fast.'

    cmd = (
        'gunicorn goldenarch:app '
        '-b "0.0.0.0:{port}" '
        '-w 16 -k gevent -t 2 '
        '--name goldenarch'
    ).format(port=PORT)
    os.system(cmd)



app = GoldenArch()

app.wsgi_app = SharedDataMiddleware(
    app.wsgi_app,
    {
        '/': os.path.join(STATIC_DIR)
    }
)

if __name__ == '__main__':
    cli()