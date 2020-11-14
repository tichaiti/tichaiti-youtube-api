from flask_restx import fields

__version__ = '0.0.1'


class Models:
    def __init__(self, api):
        self.status = api.model('Status', {
            'message': fields.String,
            'code': fields.Integer, 
            'records': fields.Integer})
        
        self.endpoint_data = api.model('EndpointData', {
            'endpoint': fields.Integer
        })
        self.endpoint_req = api.model('EndpointRequest', {
            'data': fields.List(fields.Nested(self.endpoint_data)),
            'status': fields.Nested(self.status)})
