<<<<<<< HEAD
import base64
import datetime
import picamera
import RPi.GPIO as GPIO

from time import sleep
from io import BytesIO
from socketIO_client import SocketIO, BaseNamespace

def display(msg):
    print("@"+str(datetime.datetime.now().time())+" : "+str(msg))

class Namespace(BaseNamespace):

    def on_connect(self, *args):
        display("Connected with Server")

    def on_disconnect(self, *args):
        display("Disconnected from Server\n")

display("Starting Connection with Server")
socketIO = SocketIO('192.168.43.227', 6668, Namespace)
myNamespace = socketIO.define(Namespace, '/sdc')
display("Connection Established with Server")

camera = picamera.PiCamera()
camera.resolution = (640, 320)
camera.rotation = 180
camera.start_preview()

def capture():
    myStream = BytesIO()
    camera.capture(myStream, 'jpeg')
    #camera.capture("image"+str(datetime.datetime.now().time())+".jpeg", 'jpeg')
    myString = base64.b64encode(myStream.getvalue())
    myNamespace.emit('image', {'value': str(myString)})

if __name__ == '__main__':
    display("Client Started")
    for i in range(0,250):
        display("Taking Picture "+str(i))
        capture()
    camera.stop_preview()
=======
import base64
import datetime
import picamera
import RPi.GPIO as GPIO

from time import sleep
from io import BytesIO
from socketIO_client import SocketIO, BaseNamespace

def display(msg):
    print("@"+str(datetime.datetime.now().time())+" : "+str(msg))

class Namespace(BaseNamespace):

    def on_connect(self, *args):
        display("Connected with Server")

    def on_disconnect(self, *args):
        display("Disconnected from Server\n")

display("Starting Connection with Server")
socketIO = SocketIO('192.168.43.227', 6668, Namespace)
myNamespace = socketIO.define(Namespace, '/sdc')
display("Connection Established with Server")

camera = picamera.PiCamera()
camera.resolution = (640, 320)
camera.rotation = 180
camera.start_preview()

def capture():
    myStream = BytesIO()
    camera.capture(myStream, 'jpeg')
    #camera.capture("image"+str(datetime.datetime.now().time())+".jpeg", 'jpeg')
    myString = base64.b64encode(myStream.getvalue())
    myNamespace.emit('image', {'value': str(myString)})

if __name__ == '__main__':
    display("Client Started")
    for i in range(0,250):
        display("Taking Picture "+str(i))
        capture()
    camera.stop_preview()
>>>>>>> e5e2854306b7143c1e031de516abfc66f7896142
