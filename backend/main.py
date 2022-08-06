from lib2to3.pgen2 import token
from flask import Flask, jsonify, make_response, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from service.rooms import getRoomsDb
from service.rooms import createRoom
from service.messages import getMessages,sendMessage
import jwt
import datetime

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



@app.route('/protected')
def protected():
    return jsonify({'message':'Xx secret xX'})


@socketio.on('connect')
def client_connect():
    emit('MESSAGE', messages)
    print('client connected')

@app.route('/', methods=['GET'])
def getRoomsFromRooms():
    return jsonify(getRoomsDb())

@socketio.on('disconnect')
def client_disconnect():
    print('client disconnect')

@app.route('/getMessage', methods=['GET','POST'])
def get():
    print(request.json)
    return jsonify(getMessages(request.json))

@app.route('/sendMessage', methods=['GET','POST'])
def send():
    return jsonify(sendMessage(request.json))

@app.route('/createRoom', methods=['POST'])
def create():
    return jsonify(createRoom)



@app.route('/login',methods=['POST'])
def login():
    token = jwt.encode({'user':request.json['username'],'exp':datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, app.config['SECRET_KEY'])
    return jsonify({'token':token})


if __name__ == '__main__':
    app.debug = True
    socketio.run(app, port=8080)
