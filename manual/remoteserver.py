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

angle = 10
frequency = 50

def accelerate():
    pwm = GPIO.PWM(Motor1B,frequency)
    pwm.start(angle)
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)

def reverse():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)

def left():
    #pwm = GPIO.PWM(Motor2B,frequency)
    #pwm.start(angle)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def right():
    #pwm = GPIO.PWM(Motor2A,frequency)
    #pwm.start(angle)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)

def leftTurn():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def rightTurn():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)

def leftRev():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def rightRev():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)

def brakes():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)

def release():
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)

def capture():
    camera = picamera.PiCamera()
    camera.rotation = 180
    myStream = BytesIO()
    camera.start_preview()
    camera.capture(myStream, 'jpeg')
    camera.stop_preview()
    myString = base64.b64encode(myStream.getvalue())
    return myString

app = Flask(__name__)
socketio = SocketIO(app)
socketio_connections = set()

@socketio.on('throttle', namespace='/sdc')
def on_throttle(msg):
    if msg['key']=='38':
        accelerate()
        print("@"+str(datetime.datetime.now().time())+" : Accelerate")
    elif msg['key']=='40':
        reverse()
        print("@"+str(datetime.datetime.now().time())+" : Reverse")

@socketio.on('steer', namespace='/sdc')
def on_steer(msg):
    if msg['key']=='37':
        left()
        print("@"+str(datetime.datetime.now().time())+" : Steering Left")
    elif msg['key']=='39':
        right()
        print("@"+str(datetime.datetime.now().time())+" : Steering Right")

@socketio.on('turn', namespace='/sdc')
def on_turn(msg):
    if msg['key']=='75':
        leftTurn()
        print("@"+str(datetime.datetime.now().time())+" : Turning Left")
    elif msg['key']=='77':
        rightTurn()
        print("@"+str(datetime.datetime.now().time())+" : Turning Right")

@socketio.on('reverse', namespace='sdc')
def on_reverse(msg):
    if msg['key']=='77':
        leftRev()
        print("@"+str(datetime.datetime.now().time())+" : Reversing Left")
    elif msg['key']=='79':
        rightRev()
        print("@"+str(datetime.datetime.now().time())+" : Reversing Right")

@socketio.on('brakes', namespace='/sdc')
def on_brakes(msg):
    brakes()
    print("@"+str(datetime.datetime.now().time())+" : Brakes")

@socketio.on('release', namespace='/sdc')
def on_release(msg):
    release()
    print("@"+str(datetime.datetime.now().time())+" : Released Steer")

@socketio.on('connect', namespace='/sdc')
def on_connect():
    socketio_connections.add(request.sid)
    print("@"+str(datetime.datetime.now().time())+" : Remote Connected")

@socketio.on('disconnect', namespace='/sdc')
def on_disconnect():
    socketio_connections.remove(request.sid)
    print("@"+str(datetime.datetime.now().time())+" : Remote Disconnected")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    socketio.run(app, host='192.168.43.55', port=9999)
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

angle = 10
frequency = 50

def accelerate():
    pwm = GPIO.PWM(Motor1B,frequency)
    pwm.start(angle)
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)

def reverse():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)

def left():
    #pwm = GPIO.PWM(Motor2B,frequency)
    #pwm.start(angle)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def right():
    #pwm = GPIO.PWM(Motor2A,frequency)
    #pwm.start(angle)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)

def leftTurn():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def rightTurn():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)

def leftRev():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)

def rightRev():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)

def brakes():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)

def release():
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)

def capture():
    camera = picamera.PiCamera()
    camera.rotation = 180
    myStream = BytesIO()
    camera.start_preview()
    camera.capture(myStream, 'jpeg')
    camera.stop_preview()
    myString = base64.b64encode(myStream.getvalue())
    return myString

app = Flask(__name__)
socketio = SocketIO(app)
socketio_connections = set()

@socketio.on('throttle', namespace='/sdc')
def on_throttle(msg):
    if msg['key']=='38':
        accelerate()
        print("@"+str(datetime.datetime.now().time())+" : Accelerate")
    elif msg['key']=='40':
        reverse()
        print("@"+str(datetime.datetime.now().time())+" : Reverse")

@socketio.on('steer', namespace='/sdc')
def on_steer(msg):
    if msg['key']=='37':
        left()
        print("@"+str(datetime.datetime.now().time())+" : Steering Left")
    elif msg['key']=='39':
        right()
        print("@"+str(datetime.datetime.now().time())+" : Steering Right")

@socketio.on('turn', namespace='/sdc')
def on_turn(msg):
    if msg['key']=='75':
        leftTurn()
        print("@"+str(datetime.datetime.now().time())+" : Turning Left")
    elif msg['key']=='77':
        rightTurn()
        print("@"+str(datetime.datetime.now().time())+" : Turning Right")

@socketio.on('reverse', namespace='sdc')
def on_reverse(msg):
    if msg['key']=='77':
        leftRev()
        print("@"+str(datetime.datetime.now().time())+" : Reversing Left")
    elif msg['key']=='79':
        rightRev()
        print("@"+str(datetime.datetime.now().time())+" : Reversing Right")

@socketio.on('brakes', namespace='/sdc')
def on_brakes(msg):
    brakes()
    print("@"+str(datetime.datetime.now().time())+" : Brakes")

@socketio.on('release', namespace='/sdc')
def on_release(msg):
    release()
    print("@"+str(datetime.datetime.now().time())+" : Released Steer")

@socketio.on('connect', namespace='/sdc')
def on_connect():
    socketio_connections.add(request.sid)
    print("@"+str(datetime.datetime.now().time())+" : Remote Connected")

@socketio.on('disconnect', namespace='/sdc')
def on_disconnect():
    socketio_connections.remove(request.sid)
    print("@"+str(datetime.datetime.now().time())+" : Remote Disconnected")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    socketio.run(app, host='192.168.43.55', port=9999)
    GPIO.cleanup()
>>>>>>> e5e2854306b7143c1e031de516abfc66f7896142
