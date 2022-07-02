from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from service.rooms import createRoom
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
    print(request.json)
    return jsonify(getMessages(request.json))

@app.route('/send', methods=['GET','POST'])
def send():
    return jsonify(sendMessage(request.json))

@app.route('/createRoom', methods=['POST'])
def create():
    return jsonify(createRoom)


if __name__ == '__main__':
    app.debug = True
    socketio.run(app, port=2345)
