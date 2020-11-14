from flask_restx import Namespace, Resource

import ep_example2.functions as fn
from ep_example2.models import Models


__version__ = '0.1.0'


api = Namespace('endpoint2', description='Endpoint Example 2')
models = Models(api)


@api.route('/')
class Example1(Resource):
    @api.marshal_with(models.endpoint_req)
    def get(self):
        return fn.get_data()
