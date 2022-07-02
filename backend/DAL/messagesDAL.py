from database.mongoDB import getDatabase

def getMessagesById(id):
    room = getDatabase()['room']
    messages = room.find_one({"room_id": str(id)})
    if messages is None: 
        return {'description':'not found'}
    return messages['messages']

def sendMessageFromUser(roomId, user, message, time):
    rooms = getDatabase()['room']
    rooms.update_one(
        {"room_id": str(roomId)},
        {"$push":
         {"messages": {
             "user": user,
             "message": message,
             "time_stamp": time
         }}})
    return {'status':'success'}