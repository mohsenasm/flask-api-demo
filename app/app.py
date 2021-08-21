from flask import Flask
from flask_restful import Api
from flask_apispec import FlaskApiSpec

from resources import HelloWorld, Car
from models import db

from resources import CarByName


def create_app():
    app = Flask(__name__)

    # Config
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SECRET_KEY'] = 'super_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:the_pass@db:5432/the_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # DB
    db.app = app
    db.init_app(app)
    # just for demo :)
    db.drop_all()
    db.create_all()

    # API
    api = Api(app)
    api.add_resource(HelloWorld, '/')
    api.add_resource(Car, '/car')
    api.add_resource(CarByName, '/car_by_name')

    # Spec (/swagger & /swagger-ui)
    docs = FlaskApiSpec(app)
    docs.register(Car)
    docs.register(CarByName)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=7654, host='0.0.0.0', debug=True)
