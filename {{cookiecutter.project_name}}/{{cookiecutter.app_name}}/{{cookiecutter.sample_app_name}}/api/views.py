from flask import jsonify, make_response, request
from flask_restful import Resource

from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.models import Sample, db
from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.tasks import dummy_task
from {{cookiecutter.app_name}}.utils.pagination import paginate

from .serializers import SampleSchema

"""
write Resource(ViewSet in django) in views.py
register Resource in {{cookiecutter.app_name}}.urls

"""


class SampleResource(Resource):
    def post(self):
        schema = SampleSchema()
        sample = schema.load(request.json)
        print(sample)
        object = Sample(sample)
        object.save()
        return make_response(
            jsonify(
                {
                    "message": "success",
                    "context": str(object),
                }
            ),
            200,
        )

    def get(self, id):

        schema = SampleSchema()
        object = Sample.get_by_id(id)
        return make_response(
            jsonify(
                {
                    "message": "success",
                    "data": schema.dump(object),
                }
            ),
            200,
        )

    def put(self, id):
        schema = SampleSchema(partial=True)
        object = Sample.get_by_id(id)
        object = schema.load(request.json, instance=object)
        object.save()

        return make_response(
            jsonify(
                {
                    "message": "success",
                    "data": schema.dump(object),
                }
            ),
            200,
        )

    def delete(self, id):
        object = Sample.get_by_id(id)
        object.delete()

        return make_response(
            jsonify(
                {
                    "message": "success",
                }
            ),
            200,
        )


class SampleListResource(Resource):
    def get(self):
        schema = SampleSchema(many=True)
        query = Sample.query
        # print(query.all())
        return make_response(
            jsonify(
                {
                    "message": "success",
                    "data": paginate(query, schema),
                }
            ),
            200,
        )

    def post(self):
        schema = SampleSchema()
        objects = schema.load(request.json)
        print(f"post {objects}")
        db.session.add(objects)
        db.session.commit()

        return make_response(
            jsonify(
                {
                    "message": "success",
                    "sample": schema.dump(objects),
                }
            ),
            200,
        )

class CeleryResource(Resource):
    def get(self):
        
        task_id = dummy_task.delay()
        res = task_id.get()
        return make_response(
            jsonify(
                {
                    "message": f"success, {task_id}",
                    "data": f"{res}",
                }
            ),
            200,
        )
    