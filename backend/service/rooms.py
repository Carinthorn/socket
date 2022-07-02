from database.mongoDB import getDatabase

def createRoom():
    return 'ลองใหม่ๆ'


# def createRoom(roomId, roomName):
#     rooms = database["room"]
#     rooms.insert_one(
#         {"room_id": str(roomId),
#         "room_name": str(roomName),
#         "messages": [] })
# createRoom(123, "thunroom")