# experimental runmyrobot.com client for Stepbot hardware

import RPi.GPIO as GPIO
import time
import sys
from socketIO_client import SocketIO, LoggingNamespace

GPIO.setmodel(GPIO.BOARD)

server = "runmyrobot.com"
port = 8022
robotID = None

if len(sys.argv) >= 2:
    robotID = sys.argv[1]
else:
    robotID = raw_input("Please enter your Robot ID: ")

print "Connecting to %s using SocketIO" % server
socketID = SocketIO(server, port, LoggingNamespace)
print "Connected to server"

def handle_command(args):
    print "Recieved command: ", args
    global handlingCommand

    if handlingCommand:
        print "Already handling a command, ejecting."
        return

    if "command" in args and "robot_id" in args and args["robot_id"] == robotId:
        print "Got command for tis robot", args

        command = args["command"]
        if command == "F":
            print "Got forward command"
        if command == "B":
            print "Got backward command"
        if command == "L":
            print "Got left command"
        if command == "R":
            print "Got right command"

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
