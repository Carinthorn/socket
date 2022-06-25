from operator import imod
from bson import ObjectId
import pymongo
import os
from dotenv import load_dotenv
import json


load_dotenv()

myclient = pymongo.MongoClient(os.getenv('URI'))
database = myclient["chatapp"]


def sendMessage(roomId, msg, user):
    rooms = database["room"]
    rooms.update_one(
        {"room_id": str(roomId)},
        {"$push":
         {"messages": {
             "user": user,
             "message": msg,
             "time_stamp": "10/10/2010"
         }}})
    print(rooms.find_one({"room_id": str(roomId)}))


def getMessage(roomId):
    mydb = myclient["chatapp"]["room"]
    message = [i for i in mydb.find()]
    msg = []
    for i in message:
        if i['room_id'] == roomId:
            for j in i['messages']:
                msg += [j]
            return msg
    return

def createRoom(roomId, roomName):
    rooms = database["room"]
    rooms.insert_one(
        {"room_id": str(roomId),
        "room_name": str(roomName),
        "messages": [] })
createRoom(123, "thunroom")

def thunTest():
    test = [{
        "name": "View Rooftop Bar Bangkok",
        "meal": ["snack"],
        "price":["$$$", "$$$$"],
        "location":"220 Petchaburi Road Ratchathewi, Bangkok 10400 Thailand",
        "type":["western", "american"],
        "vegan":"no",
        "imgUri":"https://cdn.discordapp.com/attachments/972401382193778701/983244910142554163/unknown.png",
        "postback":"https://viewrooftopbarbangkok.com/th/"
    },
        {
        "name": "Water Library Chamchuri",
        "meal": ["dinner"],
        "price":["$$$", "$$$$"],
        "location":"2nd floor, Chamchuri Square Samyan, Bangkok Thailand",
        "type":["western", "european"],
        "vegan":"yes",
        "imgUri":"https://cdn.discordapp.com/attachments/972401382193778701/983245107123875891/unknown.png",
        "postback":"https://th-th.facebook.com/waterlibrary/"
    },
        {
        "name": "57th Street",
        "meal": ["breakfast", "lunch", "dinner"],
        "price":["฿฿฿", "฿฿฿฿"],
        "location":"2 Sukhumvit Soi 57 Klongtan Nua, Wattana, Bangkok 10110 Thailand",
        "type":["western", "european"],
        "vegan":"yes",
        "imgUri":"https://cdn.discordapp.com/attachments/972401382193778701/983247049057255455/unknown.png",
        "postback":"https://th-th.facebook.com/waterlibrary/"
    }
    ]

    return test
