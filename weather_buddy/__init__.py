import os

from flask import Flask, jsonify

from weather_buddy.database import MongoConnector
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/users')
    def get_all_users():
        users = MongoConnector().get_collection('users')
        for user in users.find():
            user['_id'] = str(user['_id'])
        return jsonify([{
            'id': str(user['_id']),
            'zip': user['zip'],
            'name': user['name']
        } for user in users.find()])

    return app