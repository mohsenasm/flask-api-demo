from flask_restful import Resource
from flask_apispec import MethodResource, marshal_with, use_kwargs
import marshmallow as ma

from models import db, CarsModel


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class CarSchema(ma.Schema):
    name = ma.fields.Str()
    doors = ma.fields.Int()


class MessageSchema(ma.Schema):
    message = ma.fields.Str()


class Car(MethodResource, Resource):
    @marshal_with(CarSchema(many=True), code=200)
    def get(self):
        cars = CarsModel.query.all()
        return [
            {
                "name": car.name,
                "doors": car.doors
            } for car in cars]

    @use_kwargs(CarSchema)
    @marshal_with(MessageSchema, code=200)
    def post(self, **kwargs):
        if any(param not in kwargs for param in ["name", "doors"]):
            return {"message": "missed an argument"}, 400
        new_car = CarsModel(name=kwargs["name"], doors=kwargs["doors"])
        db.session.add(new_car)
        db.session.commit()
        return {"message": f"car {new_car.name} has been created successfully."}

