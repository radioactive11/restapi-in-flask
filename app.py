from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return jsonify({"get req": "this is a get request"})

    def post(self):
        data = request.json['query']
        return jsonify({"you enetred": data})

api.add_resource(Home, "/")



if __name__ == '__main__':
    app.run(debug=True)