
from flask_socketio import SocketIO, emit
from flask import Flask, render_template
from engineio.async_drivers import gevent


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = False
socketio = SocketIO(app,engineio_logger=False,log_output=False,async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/test')
def test():
    return render_template('test.html')

@socketio.on('myevent')
def test_message(message):
    emit('myresponse', {'data': 'got it!'})
    
@socketio.on('chat message')
def test_message(message):
    print('ohkay')
    emit('chat message', message)

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0",debug=True,port=443)
