import unittest
from flask_testing import TestCase
from app import create_app
from models import db


class TestBase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCar(TestBase):
    def test_car(self):
        response = self.client.post('/car', json={
            "name": "tesla",
            "doors": 4,
        })
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/car')
        response_json = response.get_json()
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response_json[0], {"name": "tesla", "doors": 4})


if __name__ == '__main__':
    unittest.main()
