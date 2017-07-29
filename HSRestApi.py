from flask import Flask, request,redirect
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///cards.db')
app = Flask(__name__)
api = Api(app)
artHSJSONURL = "https://art.hearthstonejson.com/v1/render/latest/enUS/512x/"

#select name from cards

class AllCardNames(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select name from cards")
        return {'cards': [i[0] for i in query.cursor.fetchall()]}


#select specific card and return values /cardname/leeroy%20jenkins
class CardAllDetails(Resource):
    def get(self, card_name):
        conn = db_connect.connect()
        query = conn.execute("select * from cards where lower(name) =(?)", (card_name,))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class CardBasic(Resource):
    def get(self, card_name):
        conn = db_connect.connect()
        query = conn.execute("select name,type,text,rarity,cost,attack,health,cardClass,flavor from cards where lower(name) =(?)", (card_name,))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class CardImage(Resource):
    def get(self,card_name):
        conn = db_connect.connect()
        query = conn.execute("select id from cards where lower(name) =(?)", (card_name,))
        result = query.fetchone()
        #TODO: Adjust for return value > 1 
        idURLAppend = result[0] + '.png'
        redirectURL = artHSJSONURL + idURLAppend
        #TODO: Create own image DB, don't use HSJSON Art 
        return redirect(redirectURL)

api.add_resource(AllCardNames, '/allcardnames')
api.add_resource(CardAllDetails, '/cardalldetails/<card_name>')
api.add_resource(CardBasic, '/cardbasic/<card_name>')
api.add_resource(CardImage, '/cardimage/<card_name>')

if __name__ == '__main__':
     app.run(port='5000')