from flask import Blueprint, jsonify, current_app
from flask_restful import Api
from marshmallow import ValidationError
from {{cookiecutter.app_name}}.extensions import apispec
from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.api.views import (
    SampleListResource, SampleResource)
from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.api.serializers import SampleSchema

'''
1. register api/url
2. register_views for apispec in register_views()
'''
blueprint = Blueprint('api', __name__, url_prefix='/api')
api_v1 = Api(blueprint, prefix='/v1')
api_v1.add_resource(SampleResource, '/sample/<int:id>', endpoint='sample')
api_v1.add_resource(SampleListResource, '/sample/', endpoint='samplelist')


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("SampleSchema", schema=SampleSchema)
    apispec.spec.path(view=SampleResource, app=current_app)
    return


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
