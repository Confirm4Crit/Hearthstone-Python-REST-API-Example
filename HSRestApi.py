from flask import Flask, request, redirect
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify

DB_CONNECT = create_engine('sqlite:///cards.db')
APP = Flask(__name__)
HS_API = Api(APP)
CARD_ART_BASE_URL = "https://art.hearthstonejson.com/v1/render/latest/enUS/512x/"

# TODO: Change to DOCSTRING
# select name from cards


class AllCardNames(Resource):
    def get(self):
        conn = DB_CONNECT.connect()
        query = conn.execute("select name from cards")
        return {'cards': [i[0] for i in query.cursor.fetchall()]}


# select specific card and return values /cardname/leeroy%20jenkins
class CardAllDetails(Resource):
    def get(self, card_name):
        conn = DB_CONNECT.connect()
        query = conn.execute(
            "select * from cards where lower(name) =(?)", (card_name,))
        result = {'data': [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        return jsonify(result)


class CardBasic(Resource):
    def get(self, card_name):
        conn = DB_CONNECT.connect()
        query = conn.execute(
            "select name,type,text,rarity,cost,attack,health,cardClass,flavor from cards where lower(name) =(?)", (card_name,))
        result = {'data': [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        return jsonify(result)


class CardImage(Resource):
    def get(self, card_name):
        conn = DB_CONNECT.connect()
        query = conn.execute(
            "select id from cards where lower(name) =(?)", (card_name,))
        result = query.fetchone()
        # TODO: Adjust for return value > 1
        idURLAppend = result[0] + '.png'
        redirectURL = CARD_ART_BASE_URL + idURLAppend
        # TODO: Create own image DB, don't use HSJSON Art
        return redirect(redirectURL)


HS_API.add_resource(AllCardNames, '/allcardnames')
HS_API.add_resource(CardAllDetails, '/cardalldetails/<card_name>')
HS_API.add_resource(CardBasic, '/cardbasic/<card_name>')
HS_API.add_resource(CardImage, '/cardimage/<card_name>')

if __name__ == '__main__':
    APP.run(port='5000')
