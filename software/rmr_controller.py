# experimental runmyrobot.com client for Stepbot hardware

#import RPi.GPIO as GPIO
import time
import sys
import thread
import subprocess
from socketIO_client import SocketIO, LoggingNamespace

# Begin Stepbot-specific code

#GPIO.setmode(GPIO.BOARD)

# motor 1
coil_A_1_pin = 24
coil_A_2_pin = 16
coil_B_1_pin = 18
coil_B_2_pin = 22

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# motor 2
coil_C_1_pin = 11 
coil_C_2_pin = 13
coil_D_1_pin = 15
coil_D_2_pin = 21

GPIO.setup(coil_C_1_pin, GPIO.OUT)
GPIO.setup(coil_C_2_pin, GPIO.OUT)
GPIO.setup(coil_D_1_pin, GPIO.OUT)
GPIO.setup(coil_D_2_pin, GPIO.OUT)

def m1Forward(delay, steps):
    for i in range(0, steps):
        m1SetStep(0,0,1,1)
        time.sleep(delay)
        m1SetStep(1,0,0,1)
        time.sleep(delay)
        m1SetStep(1,1,0,0)
        time.sleep(delay)
        m1SetStep(0,1,1,0)
        time.sleep(delay)

def m1Backwards(delay, steps):
    for i in range(0, steps):
        m1SetStep(0,1,1,0)
        time.sleep(delay)
        m1SetStep(1,1,0,0)
        time.sleep(delay)
        m1SetStep(1,0,0,1)
        time.sleep(delay)
        m1SetStep(0,0,1,1)
        time.sleep(delay)

def m1SetStep(w1,w2,w3,w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def m2Forward(delay, steps):
    for i in range(0, steps):
        m2SetStep(0,1,1,0)
        time.sleep(delay)
        m2SetStep(1,1,0,0)
        time.sleep(delay)
        m2SetStep(1,0,0,1)
        time.sleep(delay)
        m2SetStep(0,0,1,1)
        time.sleep(delay)

def m2Backwards(delay, steps):
    for i in range(0, steps):
        m2SetStep(0,0,1,1)
        time.sleep(delay)
        m2SetStep(1,0,0,1)
        time.sleep(delay)
        m2SetStep(1,1,0,0)
        time.sleep(delay)
        m2SetStep(0,1,1,0)
        time.sleep(delay)

def m2SetStep(w1,w2,w3,w4):
    GPIO.output(coil_C_1_pin, w1)
    GPIO.output(coil_C_2_pin, w2)
    GPIO.output(coil_D_1_pin, w3)
    GPIO.output(coil_D_2_pin, w4)

def forward(steps):
    for i in range(0, steps):
        m1Forward(2.0/1000.0,1)
        m2Forward(2.0/1000.0,1)

def backward(steps):
    for i in range(0, steps):
        m1Backwards(2.0/1000.0,1)
        m2Backwards(2.0/1000.0,1)

def turnRight(steps):
    for i in range(0, steps):
        m1Backwards(2.0/1000.0,1)
        m2Forward(2.0/1000.0,1)

def turnLeft(steps):
    for i in range(0, steps):
        m2Backwards(2.0/1000.0,1)
        m1Forward(2.0/1000.0,1)


# Begin runmyrobot.com code

server = "runmyrobot.com"
port = 8022
robotID = None
handlingCommand = False

if len(sys.argv) >= 2:
    robotID = sys.argv[1]
else:
    robotID = raw_input("Please enter your Robot ID: ")

print "Connecting to %s using SocketIO" % server
socketIO = SocketIO(server, port, LoggingNamespace)
print "Connected to server"

def handle_command(args):
    #print "Recieved command: ", args
    global handlingCommand

    if handlingCommand:
        print "Already handling a command, ejecting."
        return

    if "command" in args and "robot_id" in args and args["robot_id"] == robotID:
        print "Got command for tis robot", args

        command = args["command"]
        if command == "F":
            print "Got forward command"
            forward(10)
        if command == "B":
            print "Got backward command"
            backward(10)
        if command == "L":
            print "Got left command"
            turnLeft(10)
        if command == "R":
            print "Got right command"
            turnRight(10)

        handlingCommand = False

def on_handle_command(*args):
    thread.start_new_thread(handle_command, args)

socketIO.on("command_to_robot", on_handle_command)

def ipInfoUpdate():
    socketIO.emit("ip_information", {"ip": subprocess.check_output(["hostname", "-I"]), "robot_id": robotID})

def identifyRobotId():
    socketIO.emit("identify_robot_id", robotID)

# this is where thing get started
identifyRobotId()
ipInfoUpdate()
waitCounter = 0

while True:
    socketIO.wait(seconds=10)
    if(waitCounter % 10) == 0:
        ipInfoUpdate()
        
    waitCounter += 1
