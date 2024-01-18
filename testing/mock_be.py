from flask import Flask, Response, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Session(Resource):
    def get(self):
        print(request.headers)
        msg = "SESSION_ID_BE"
        response = Response(msg,content_type="text/plain; charset=utf-8" )
        return response

class Chat(Resource):
    def post(self):
        print("head", request.headers)
        print('body', request.json)
        msg = "This is a mock response"
        response = Response(msg,content_type="text/plain; charset=utf-8" )
        return response

api.add_resource(Session, '/session') 

api.add_resource(Chat, '/chat') 

if __name__ == '__main__':
    app.run()