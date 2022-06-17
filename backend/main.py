from flask import Flask,jsonify
from database.dbconnection import sendMessage
from database.dbconnection import getMessage
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'mysecret'


@app.route('/get/<roomId>', methods=['GET'])
def get(roomId=0):
    return jsonify(getMessage(roomId))

@app.route('/send/<roomId>', methods=['POST'])
def test(roomId=0):
    return jsonify(sendMessage(roomId, "hello"))

if __name__ == '__main__':
	app.run(threaded=True, port=5050)


# 	from flask import Flask, render_template, request, redirect, url_for, session
# from flask_socketio import SocketIO, join_room, leave_room, emit
# from flask_session import Session

# app = Flask(__name__)
# app.debug = True
# app.config['SECRET_KEY'] = 'secret'
# app.config['SESSION_TYPE'] = 'filesystem'

# Session(app)

# socketio = SocketIO(app, manage_session=False)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['GET', 'POST'])
# def chat():
#     if(request.method=='POST'):
#         username = request.form['username']
#         room = request.form['room']
#         #Store the data in session
#         session['username'] = username
#         session['room'] = room
#         return render_template('chat.html', session = session)
#     else:
#         if(session.get('username') is not None):
#             return render_template('chat.html', session = session)
#         else:
#             return redirect(url_for('index'))

# @socketio.on('join', namespace='/chat')
# def join(message):
#     room = session.get('room')
#     join_room(room)
#     emit('status', {'msg':  session.get('username') + ' has entered the room.'}, room=room)


# @socketio.on('text', namespace='/chat')
# def text(message):
#     room = session.get('room')
#     emit('message', {'msg': session.get('username') + ' : ' + message['msg']}, room=room)


# @socketio.on('left', namespace='/chat')
# def left(message):
#     room = session.get('room')
#     username = session.get('username')
#     leave_room(room)
#     session.clear()
#     emit('status', {'msg': username + ' has left the room.'}, room=room)


# if __name__ == '__main__':
#     socketio.run(app)