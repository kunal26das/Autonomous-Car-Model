<<<<<<< HEAD
import base64
import datetime
import picamera
import RPi.GPIO as GPIO

from io import BytesIO
from flask import Flask, request
from flask_socketio import SocketIO, emit

#Rear Wheels for Driving
Motor1A = 23
Motor1B = 24

#Front Wheels for Steer
Motor2A = 26
Motor2B = 19

def accelerate():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)

def reverse():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)

def left():
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def right():
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)

def brakes():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)

def release():
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)

app = Flask(__name__)
socketio = SocketIO(app)
socketio_connections = set()

def display(msg):
    print("@"+str(datetime.datetime.now().time())+" : "+str(msg))

@socketio.on('accelerate', namespace='/sdc')
def on_accelerate(msg):
    accelerate()
    display("Accelerating")

@socketio.on('left', namespace='/sdc')
def on_left(msg):
    left()
    display("Turning Left")

@socketio.on('right', namespace='/sdc')
def on_right(msg):
    right()
    display("Turning Right")

@socketio.on('brakes', namespace='/sdc')
def on_brakes(msg):
    brakes()
    display("Applied Brakes")

@socketio.on('release', namespace='/sdc')
def on_release(msg):
    release()
    display("Released Steer")

@socketio.on('connect', namespace='/sdc')
def on_connect():
    socketio_connections.add(request.sid)
    display("Remote Connected")

@socketio.on('disconnect', namespace='/sdc')
def on_disconnect():
    socketio_connections.remove(request.sid)
    display("Remote Disconnected")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    #GPIO.setwarnings(False)
    socketio.run(app, host='192.168.43.55', port=6666)
    GPIO.cleanup()
=======
import base64
import datetime
import picamera
import RPi.GPIO as GPIO

from io import BytesIO
from flask import Flask, request
from flask_socketio import SocketIO, emit

#Rear Wheels for Driving
Motor1A = 23
Motor1B = 24

#Front Wheels for Steer
Motor2A = 26
Motor2B = 19

def accelerate():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)

def reverse():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)

def left():
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def right():
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)

def brakes():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)

def release():
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)

app = Flask(__name__)
socketio = SocketIO(app)
socketio_connections = set()

def display(msg):
    print("@"+str(datetime.datetime.now().time())+" : "+str(msg))

@socketio.on('accelerate', namespace='/sdc')
def on_accelerate(msg):
    accelerate()
    display("Accelerating")

@socketio.on('left', namespace='/sdc')
def on_left(msg):
    left()
    display("Turning Left")

@socketio.on('right', namespace='/sdc')
def on_right(msg):
    right()
    display("Turning Right")

@socketio.on('brakes', namespace='/sdc')
def on_brakes(msg):
    brakes()
    display("Applied Brakes")

@socketio.on('release', namespace='/sdc')
def on_release(msg):
    release()
    display("Released Steer")

@socketio.on('connect', namespace='/sdc')
def on_connect():
    socketio_connections.add(request.sid)
    display("Remote Connected")

@socketio.on('disconnect', namespace='/sdc')
def on_disconnect():
    socketio_connections.remove(request.sid)
    display("Remote Disconnected")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    #GPIO.setwarnings(False)
    socketio.run(app, host='192.168.43.55', port=6666)
    GPIO.cleanup()
>>>>>>> e5e2854306b7143c1e031de516abfc66f7896142
