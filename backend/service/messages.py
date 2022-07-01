from database.mongoDB import getDatabase
import datetime

def getMessages(data):
    room = getDatabase()['room']
    messages = room.find_one({"room_id": str(data['roomId'])})
    return messages['messages']

def sendMessage(data):
    rooms = getDatabase()['room']
    rooms.update_one(
        {"room_id": str(data['roomId'])},
        {"$push":
         {"messages": {
             "user": data['user'],
             "message": data['message'],
             "time_stamp": datetime.datetime.now()
         }}})
    return {'status':'success'}