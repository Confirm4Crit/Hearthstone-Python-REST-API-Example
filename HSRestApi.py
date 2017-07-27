from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///cards.db')
app = Flask(__name__)
api = Api(app)

#select name from cards

class AllCardNames(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select name from cards")
        return {'cards': [i[0] for i in query.cursor.fetchall()]}


#select specific card and return values /cardname/leeroy%20jenkins
class CardName(Resource):
    def get(self, card_name):
        conn = db_connect.connect()
        query = conn.execute("select * from cards where lower(name) =(?)", (card_name,))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(AllCardNames, '/allcardnames')
api.add_resource(CardName, '/cardname/<card_name>')

if __name__ == '__main__':
     app.run(port='5000')