from operator import imod
import pymongo
import os
from dotenv import load_dotenv
import json


load_dotenv()

myclient = pymongo.MongoClient(os.getenv('URI'))


def sendMessage(roomId,msg):
    rooms = myclient["chatapp"]["room"]
    rooms.update({'roomId': roomId}, {'$push': {'messages': {
        'user':'pete',
        'message': msg,
        'time_stamp':'10/10/2010'
    }}})

    
            


def getMessage(roomId):
    mydb = myclient["chatapp"]["room"]
    message = [i for i in mydb.find()]
    msg = []
    for i in message:
        if i['room_id'] == roomId:
            for j in i['messages']:
                msg += [j]
            return msg
    return "not found"


sendMessage("12345", "hiiiiiiiiiiiiiiiiiiiii")
