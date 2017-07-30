from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
DB_CONNECT = SQLAlchemy(app)
#Test model for db
class CardModel(DB_CONNECT.Model):
    __tablename__ = 'cards'
    artist	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    attack	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    cardClass	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    collectible	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    cost	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    dbfId	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    flavor	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    health	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    id	= DB_CONNECT.Column(DB_CONNECT.String(255), primary_key=True)
    name	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playerClass	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    rarity	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    referencedTags	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    set	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    text = DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    type	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    elite	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    mechanics	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    howToEarnGolden	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    race	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_MINION_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_TO_PLAY	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    howToEarn	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_MIN_ATTACK	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    mechanics_1	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    targetingArrow= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    durability	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_ENEMY_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_NUM_MINION_SLOTS	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_MAX_ATTACK	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_0	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_1	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    faction	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_FRIENDLY_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_NONSELF_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_IF_AVAILABLE	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_WITH_DEATHRATTLE	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_2	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_3	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_4	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_5	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_6	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_7	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_8	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_9	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_WITH_RACE	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_HERO_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_IF_AVAILABLE_AND_DRAGON_IN_HAND	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_SECRET_ZONE_CAP_FOR_NON_SECRET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    overload	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_MINIMUM_ENEMY_MINIONS	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    spellDamage	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    hideStats	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    classes_0	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    classes_1	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    classes_2	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    multiClassGroup	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_STEALTHED_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_FOR_COMBO	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_FROZEN_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    referencedTags_1	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    collection = DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_MINION_SLOT_OR_MANA_CRYSTAL_SLOT	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    mechanics_2	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    mechanics_3	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_LEGENDARY_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_MUST_TARGET_TAUNTER	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_IF_AVAILABE_AND_ELEMENTAL_PLAYED_LAST_TURN	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_IF_AVAILABLE_AND_MINIMUM_FRIENDLY_MINIONS	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_MINIMUM_TOTAL_MINIONS	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_WEAPON_EQUIPPED	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_TARGET_IF_AVAILABLE_AND_MINIMUM_FRIENDLY_SECRETS	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_DAMAGED_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_ENEMY_WEAPON_EQUIPPED	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_UNDAMAGED_TARGET	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_ENTIRE_ENTOURAGE_NOT_IN_PLAY	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_MINION_OR_ENEMY_HERO	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_STEADY_SHOT	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_10	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_11	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_12	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_13	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_14	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_15	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_16	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_17	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_18	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_19	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_20	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_21	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_22	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_23	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_24	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_25	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_26	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_27	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_28	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_29	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_30	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_31	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_32	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_33	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_34	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_35	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_36	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_37	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_38	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_39	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_40	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_41	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_42	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_43	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_44	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_45	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_46	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_47	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_48	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_49	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_50	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_51	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_52	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_53	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_54	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_55	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_56	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_57	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_58	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    entourage_59	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    playRequirements_REQ_FRIENDLY_MINION_DIED_THIS_GAME	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    referencedTags_2	= DB_CONNECT.Column(DB_CONNECT.String(255), unique=False)
    

    def __init__(self, dbfId, name):
        self.dbfId = dbfId
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.Name