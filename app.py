from flask import Flask
from flask_restful import Resource, Api
from PIL import Image

app = Flask(__name__)
api = Api(app)

class Api(Resource):
    def get(self):
        return { 'data': True }, 200

api.add_resource(Api, '/is-alive')

if __name__ == '__main__':
    app.run()  # run our Flask app