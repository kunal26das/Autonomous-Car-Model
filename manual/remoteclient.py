<<<<<<< HEAD
import datetime
from tkinter import *
from socketIO_client import SocketIO, BaseNamespace

class Namespace(BaseNamespace):

    def on_connect(self, *args):
        print("@"+str(datetime.datetime.now().time())+" : Car Connected")

    def on_disconnect(self, *args):
        print("@"+str(datetime.datetime.now().time())+" : Car Disconnected \n")

socketIO = SocketIO('192.168.43.55', 9999, Namespace)
myNamespace = socketIO.define(Namespace, '/sdc')

flagUp = False
flagDown = False
flagLeft = False
flagRight = False

def keyPressUp(e):
    global flagUp
    global myNamespace
    if flagUp==False:
        myNamespace.emit('throttle', {'key': str(e.keycode)})
        flagUp=True

def keyReleaseUp(e):
    global flagUp
    global myNamespace
    if flagUp==True:
        myNamespace.emit('brakes', {'key': str(e.keycode)})
        flagUp=False

def keyPressDown(e):
    global flagDown
    global myNamespace
    if flagDown==False:
        myNamespace.emit('throttle', {'key': str(e.keycode)})
        flagDown=True

def keyReleaseDown(e):
    global flagDown
    global myNamespace
    if flagDown==True:
        myNamespace.emit('brakes', {'key': str(e.keycode)})
        flagDown=False

def keyPressLeft(e):
    global flagLeft
    global myNamespace
    if flagLeft==False:
        myNamespace.emit('steer', {'key': str(e.keycode)})
        flagLeft=True

def keyReleaseLeft(e):
    global flagLeft
    global myNamespace
    if flagLeft==True:
        myNamespace.emit('release', {'key': str(e.keycode)})
        flagLeft=False

def keyPressRight(e):
    global flagRight
    global myNamespace
    if flagRight==False:
        myNamespace.emit('steer', {'key': str(e.keycode)})
        flagRight=True

def keyReleaseRight(e):
    global flagRight
    global myNamespace
    if flagRight==True:
        myNamespace.emit('release', {'key': str(e.keycode)})
        flagRight=False

if __name__ == '__main__':
    print("@"+str(datetime.datetime.now().time())+" : Remote client started")

    window = Tk()
    window.title("Self Driving Car")
    window.bind("<KeyPress-Up>", keyPressUp)
    window.bind("<KeyRelease-Up>", keyReleaseUp)
    window.bind("<KeyPress-Down>", keyPressDown)
    window.bind("<KeyRelease-Down>", keyReleaseDown)
    window.bind("<KeyPress-Left>", keyPressLeft)
    window.bind("<KeyRelease-Left>", keyReleaseLeft)
    window.bind("<KeyPress-Right>", keyPressRight)
    window.bind("<KeyRelease-Right>", keyReleaseRight)
    window.mainloop()
=======
import datetime
from tkinter import *
from socketIO_client import SocketIO, BaseNamespace

class Namespace(BaseNamespace):

    def on_connect(self, *args):
        print("@"+str(datetime.datetime.now().time())+" : Car Connected")

    def on_disconnect(self, *args):
        print("@"+str(datetime.datetime.now().time())+" : Car Disconnected \n")

socketIO = SocketIO('192.168.43.55', 9999, Namespace)
myNamespace = socketIO.define(Namespace, '/sdc')

flagUp = False
flagDown = False
flagLeft = False
flagRight = False

def keyPressUp(e):
    global flagUp
    global myNamespace
    if flagUp==False:
        myNamespace.emit('throttle', {'key': str(e.keycode)})
        flagUp=True

def keyReleaseUp(e):
    global flagUp
    global myNamespace
    if flagUp==True:
        myNamespace.emit('brakes', {'key': str(e.keycode)})
        flagUp=False

def keyPressDown(e):
    global flagDown
    global myNamespace
    if flagDown==False:
        myNamespace.emit('throttle', {'key': str(e.keycode)})
        flagDown=True

def keyReleaseDown(e):
    global flagDown
    global myNamespace
    if flagDown==True:
        myNamespace.emit('brakes', {'key': str(e.keycode)})
        flagDown=False

def keyPressLeft(e):
    global flagLeft
    global myNamespace
    if flagLeft==False:
        myNamespace.emit('steer', {'key': str(e.keycode)})
        flagLeft=True

def keyReleaseLeft(e):
    global flagLeft
    global myNamespace
    if flagLeft==True:
        myNamespace.emit('release', {'key': str(e.keycode)})
        flagLeft=False

def keyPressRight(e):
    global flagRight
    global myNamespace
    if flagRight==False:
        myNamespace.emit('steer', {'key': str(e.keycode)})
        flagRight=True

def keyReleaseRight(e):
    global flagRight
    global myNamespace
    if flagRight==True:
        myNamespace.emit('release', {'key': str(e.keycode)})
        flagRight=False

if __name__ == '__main__':
    print("@"+str(datetime.datetime.now().time())+" : Remote client started")

    window = Tk()
    window.title("Self Driving Car")
    window.bind("<KeyPress-Up>", keyPressUp)
    window.bind("<KeyRelease-Up>", keyReleaseUp)
    window.bind("<KeyPress-Down>", keyPressDown)
    window.bind("<KeyRelease-Down>", keyReleaseDown)
    window.bind("<KeyPress-Left>", keyPressLeft)
    window.bind("<KeyRelease-Left>", keyReleaseLeft)
    window.bind("<KeyPress-Right>", keyPressRight)
    window.bind("<KeyRelease-Right>", keyReleaseRight)
    window.mainloop()
>>>>>>> e5e2854306b7143c1e031de516abfc66f7896142
