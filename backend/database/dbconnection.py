from operator import imod
from bson import ObjectId
import pymongo
import os
from dotenv import load_dotenv
import json


load_dotenv()

myclient = pymongo.MongoClient(os.getenv('URI'))
database = myclient["chatapp"]


def sendMessage(roomId, msg):
    rooms = database["room"]
    rooms.update_one(
        {"room_id": str(roomId)},
        {"$push":
         {"messages": {
             "user": "pete",
             "message": "hasdasdasd",
             "time_stamp": "10/10/2010"
         }}})
    print(rooms.find_one({"room_id":str(roomId)}))


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


sendMessage("12345", "asdasd")
