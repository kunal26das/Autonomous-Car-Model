<<<<<<< HEAD
import utils
import base64
import datetime
import numpy as np

from PIL import Image
from io import BytesIO
from flask_socketio import emit
from flask import Flask, request
from keras.models import load_model
from socketIO_client import BaseNamespace
from flask_socketio import SocketIO as fsio
from socketIO_client import SocketIO as sioc

app = Flask(__name__)
serverSocket = fsio(app)
socketio_connections = set()

def display(msg):
    print("@"+str(datetime.datetime.now().time())+" : "+str(msg))

class Namespace(BaseNamespace):

    def on_connect(self, *args):
        display("Connected with Remote Server")

    def on_disconnect(self, *args):
        display("Disconnected from Remote Server\n")

model = load_model("model.h5")
clientSocket = sioc('192.168.43.55', 6666, Namespace)
myNamespace = clientSocket.define(Namespace, '/sdc')

def send_control(steering_angle):
    steering_angle = 100*steering_angle
    #steering_angle = 100
    if steering_angle > 0:
        #steering_angle = int(round(steering_angle))
        myNamespace.emit('right', {})
        #right
    elif steering_angle < 0:
        steering_angle = -1*steering_angle
        #steering_angle = int(round(steering_angle))
        myNamespace.emit('left', {})
        #left
    else:
        myNamespace.emit('release', {})

@serverSocket.on('connect', namespace='/sdc')
def on_connect():
    socketio_connections.add(request.sid)
    display("Connected with Image Client")
    display("Starting Car")
    myNamespace.emit('accelerate', {})

@serverSocket.on('disconnect', namespace='/sdc')
def on_disconnect():
    socketio_connections.remove(request.sid)
    display("Disconnected from Image Client")
    display("Stopping Car")
    myNamespace.emit('brakes', {})

@serverSocket.on('image', namespace='/sdc')
def on_image(msg):
    display("Received Image from Client")
    myString = base64.b64decode(msg['value'])
    myStream = BytesIO(myString)
    image = Image.open(myStream)
    image = np.asarray(image)
    image = utils.preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image, batch_size=1))
    display(steering_angle)
    send_control(steering_angle)

if __name__ == '__main__':
    display("Server Started")
    serverSocket.run(app, host='192.168.43.227', port=6668)
=======
import utils
import base64
import datetime
import numpy as np

from PIL import Image
from io import BytesIO
from flask_socketio import emit
from flask import Flask, request
from keras.models import load_model
from socketIO_client import BaseNamespace
from flask_socketio import SocketIO as fsio
from socketIO_client import SocketIO as sioc

app = Flask(__name__)
serverSocket = fsio(app)
socketio_connections = set()

def display(msg):
    print("@"+str(datetime.datetime.now().time())+" : "+str(msg))

class Namespace(BaseNamespace):

    def on_connect(self, *args):
        display("Connected with Remote Server")

    def on_disconnect(self, *args):
        display("Disconnected from Remote Server\n")

model = load_model("model.h5")
clientSocket = sioc('192.168.43.55', 6666, Namespace)
myNamespace = clientSocket.define(Namespace, '/sdc')

def send_control(steering_angle):
    steering_angle = 100*steering_angle
    #steering_angle = 100
    if steering_angle > 0:
        #steering_angle = int(round(steering_angle))
        myNamespace.emit('right', {})
        #right
    elif steering_angle < 0:
        steering_angle = -1*steering_angle
        #steering_angle = int(round(steering_angle))
        myNamespace.emit('left', {})
        #left
    else:
        myNamespace.emit('release', {})

@serverSocket.on('connect', namespace='/sdc')
def on_connect():
    socketio_connections.add(request.sid)
    display("Connected with Image Client")
    display("Starting Car")
    myNamespace.emit('accelerate', {})

@serverSocket.on('disconnect', namespace='/sdc')
def on_disconnect():
    socketio_connections.remove(request.sid)
    display("Disconnected from Image Client")
    display("Stopping Car")
    myNamespace.emit('brakes', {})

@serverSocket.on('image', namespace='/sdc')
def on_image(msg):
    display("Received Image from Client")
    myString = base64.b64decode(msg['value'])
    myStream = BytesIO(myString)
    image = Image.open(myStream)
    image = np.asarray(image)
    image = utils.preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image, batch_size=1))
    display(steering_angle)
    send_control(steering_angle)

if __name__ == '__main__':
    display("Server Started")
    serverSocket.run(app, host='192.168.43.227', port=6668)
>>>>>>> e5e2854306b7143c1e031de516abfc66f7896142
