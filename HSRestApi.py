from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///cards.db')
app = Flask(__name__)
api = Api(app)

#select name from cards

class CardNames(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select name from cards")
        return {'cards': [i[0] for i in query.cursor.fetchall()]}

api.add_resource(CardNames, '/cardnames') # Route_1

if __name__ == '__main__':
     app.run(port='5002')