from flask_restx import Namespace, Resource

from ep_example1.models import Models


__version__ = '0.1.0'


api = Namespace('endpoint1', description='Endpoint Example 1')
models = Models(api)


@api.route('/')
class Example1(Resource):
    @api.marshal_with(models.endpoint_req)
    def get(self):
        d = {
                'data': [
                    {'endpoint': 1}
                ],
                'status': {
                    'message': 'OK',
                    'code': 200,
                    'records': 1
                }
        }
        return d
