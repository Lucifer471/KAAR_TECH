from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymongo

client = pymongo.MongoClient("mongodb+srv://Rishi_AB:Rishiv2k@cluster0.x1ku8vn.mongodb.net/?retryWrites=true&w=majority")
db = client.test


app = Flask(__name__)

api = Api(app)

class Hello(Resource):

    def get(self):

        return jsonify({'HEY THERE !!,':'HOW WAS YOUR DAY'})

    def post(self):

        data = request.get_json()
        return jsonify({'data': data}), 201


class Cube(Resource):

    def get(self, num):

        return jsonify({f'CUBE OF {num}': num**3})

class Square(Resource):

    def get(self, num):

        return jsonify({f'SQUARE OF {num}': num**2})

api.add_resource(Hello, '/')
api.add_resource(Cube, '/cube/<int:num>')
api.add_resource(Square, '/square/<int:num>')


if __name__ == '__main__':

    app.run(debug = True)