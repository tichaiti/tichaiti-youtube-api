#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from ep_example1.endpoints import api as endpoint1
from ep_example2.endpoints import api as endpoint2

__version__ = '0.1.0'

base_url = '/'

app = Flask(__name__)
api = Api(
    app, 
    doc=f'{base_url}/', 
    prefix=base_url,
    title='Endpoint Template', 
    version=__version__)
CORS(app)

api.add_namespace(endpoint1)
api.add_namespace(endpoint2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
