from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, doors):
        self.name = name
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"
