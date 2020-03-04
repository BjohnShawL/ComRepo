""""Main entrypoint for the tags API"""
import json
import os
import shelve
import markdown
from flask import Flask, g, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

from models import POSTGRES_DB

APP = Flask(__name__)
API = Api(APP)

_db = POSTGRES_DB.init_app(APP)

def get_db():
    """Opens the database connection to shelf"""
    if 'db' not in g:
        g.db = shelve.open("power_tags.db")

    return g.db

@APP.teardown_appcontext
def teardown_db(exception):
    """Closes the databse connection on exception"""
    db = g.pop('db', None)

    if db is not None:
        db.close()

@APP.route('/')
def index():
    """Show the documentation for the tags api"""
    with open(os.path.dirname(APP.root_path)+ '/README.md', 'r') as d_file:
        content = d_file.read()
        return markdown.markdown(content)

class Tags(Resource):
    """Defines the 'Tags' endpoint for the API """
    def get(self):
        """Get all tags"""
        shelf = get_db()
        keys = list(shelf.keys())

        tags = []

        for key in keys:
            tags.append(shelf[key])
        return {
            "message":"tag listing returned",
            "data": tags}, 200, {"Access-Control-Allow-Origin": "http://localhost:3000"}

    def post(self):
        """Post new tag to tags collection"""
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('character', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('max_use', type=int, required=True)
        parser.add_argument('current_use', type=int, required=True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {"message":"Power Tag created", "data":args}, 201
    def options(self):
        """Options method for CORS"""
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response
class Tag(Resource):
    """Defines a singular Tag"""
    def get(self, identifier):
        """returns data concerning the particular tag indicated"""
        shelf = get_db()
        if not identifier in shelf:
            return {"message":"Tag not found", "data":{}}, 404
        return {"message":"Tag found", "data":shelf[identifier]}
    def delete(self, identifier):
        """Deletes a particular tag"""
        shelf = get_db()
        if not identifier in shelf:
            return {"message":"Tag not found", "data":{}}, 404
        del shelf[identifier]
        return '', 204
    def put(self, identifier):
        """updates the 'current_use' key of the identified tag"""
        shelf = get_db()

        value = request.json

        # parser = reqparse.RequestParser()
        # parser.add_argument('current_use', type=int, required=True)
        # args = parser.parse_args()

        if not identifier in shelf:
            return {"message":"Tag not found", "data":{}}, 404
        data = shelf[identifier]
        data['current_use'] = value['current_use']
        shelf[identifier] = data
        return{"message":"Tag updated", "data":data['current_use']}, 200

API.add_resource(Tags, '/tags')
API.add_resource(Tag, '/tag/<string:identifier>')
