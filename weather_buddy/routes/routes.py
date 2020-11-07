from flask import Blueprint, jsonify

from weather_buddy.database import MongoConnector

routes = Blueprint('routes', __name__)

# a simple page that says hello
@routes.route('/hello')
def hello():
    return 'Hello, World!'

@routes.route('/users')
def get_all_users():
    users = MongoConnector().get_collection('users')
    for user in users.find():
        user['_id'] = str(user['_id'])
    return jsonify([{
        'id': str(user['_id']),
        'zip': user['zip'],
        'name': user['name']
    } for user in users.find()])