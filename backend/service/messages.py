from DAL.messagesDAL import getMessagesById, sendMessageFromUser
import datetime

def getMessages(data):
    id = data['roomId']
    return getMessagesById(id)


def sendMessage(data):
    roomId = data['roomId']
    user = data['user']
    message = data['message']
    contry = data['contry']
    time = datetime.datetime.now()
    return sendMessageFromUser(roomId, user, message, time)
