# from flask import Flask, jsonify
# from database.dbconnection import createRoom
# from database.dbconnection import thunTest
# from database.dbconnection import sendMessage
# from database.dbconnection import getMessage
# from flask_cors import CORS, cross_origin
# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['SECRET_KEY'] = 'mysecret'


# @app.route('/get/<roomId>', methods=['GET'])
# def get(roomId=0):
#     return jsonify(getMessage(roomId))


# @app.route('/send/<roomId>:<msg>:<user>', methods=['POST'])
# def test(roomId=0,msg="",user=""):
#     return jsonify(sendMessage(roomId, msg, user))

# @app.route('/create_room/<roomId>:<roomName>', methods=['POST'])
# def create(roomId=0,roomName=""):
#     return jsonify(createRoom(roomId, roomName))

# @app.route('/test', methods=['GET'])
# def thun():
#     return jsonify(thunTest())


# if __name__ == '__main__':
#     app.run(threaded=True, port=5050)


from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from service.messages import getMessages,sendMessage

app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'secret'
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app,cors_allowed_origins='*')

messages = [
    {
        'color': 'red',
        'user': 'user1',
        'msg': 'heelo',
    },
    {
        'color': 'blue',
        'user': 'user2',
        'msg': 'test',
    }
]


@socketio.on('connect')
def client_connect():
    emit('MESSAGE', messages)
    print('client connected')


@socketio.on('disconnect')
def client_disconnect():
    print('client disconnect')

@app.route('/get', methods=['GET','POST'])
def get():
    return jsonify(getMessages(request.json))

@app.route('/send', methods=['GET','POST'])
def send():
    return jsonify(sendMessage(request.json))


if __name__ == '__main__':
    app.debug = True
    socketio.run(app, port=2345)
