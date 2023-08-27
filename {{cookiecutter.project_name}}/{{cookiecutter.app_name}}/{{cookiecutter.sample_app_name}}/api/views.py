from flask import jsonify, make_response, request
from flask_restful import Resource, abort

from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.models import Sample, db
from {{cookiecutter.app_name}}.{{cookiecutter.sample_app_name}}.tasks import dummy_task
from {{cookiecutter.app_name}}.utils.pagination import paginate

from .serializers import SampleSchema, SampleUrlParamSchema

"""
write Resource(ViewSet in django) in views.py
register Resource in {{cookiecutter.app_name}}.urls

"""


class SampleResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      summary: Get a user
      description: Get a single user by ID
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  user: SampleSchema
        404:
          description: user does not exists
    put:
      tags:
        - api
      summary: Update a user
      description: Update a single user by ID
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              SampleSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: user updated
                  user: SampleSchema
        404:
          description: user does not exists
    delete:
      tags:
        - api
      summary: Delete a user
      description: Delete a single user by ID
      parameters:
        - in: path
          name: id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: user deleted
        404:
          description: user does not exists
    """
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
    """Creation and get_all

    ---
    get:
      tags:
        - api
      summary: Get a list of users
      description: Get a list of paginated users
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/UserSchema'
    post:
      tags:
        - api
      summary: Create a user
      description: Create a new user
      requestBody:
        content:
          application/json:
            schema:
              UserSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: user created
                  user: UserSchema
    """
    def get(self):
        url_data = request.args
        url_schema = SampleUrlParamSchema()
        
        errors = url_schema.validate(url_data) # if no specific abort() is needed, this .validate() could be skipped #noqa
        if errors:
            abort(404, error=str(errors))
            
            
        url_param = url_schema.load(url_data)
        schema = SampleSchema(many=True)
        query = Sample.query
        query_set = query.filter_by(**url_param)
        return make_response(
            jsonify(
                {
                    "message": "success",
                    "data": paginate(query_set, schema),
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
    