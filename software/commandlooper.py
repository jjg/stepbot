import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

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

def turn(steps):
    for i in range(0, steps):
        m1Backwards(2.0/1000.0,1)
        m2Forward(2.0/1000.0,1)

stepsForward = raw_input("How many steps forward?")
stepsTurn = raw_input("How many steps to turn?")
stepsBackward = raw_input("How many steps backward?")

while True:
    #delay = raw_input("Delay between steps (ms)?")
    #stepsForward = raw_input("How many steps forward?")
    forward(int(stepsForward))
    #stepsBackward = raw_input("How many steps backward?")
    backward(int(stepsBackward))
    #stepsTurn = raw_input("How many steps to turn?")
    turn(int(stepsTurn))
    #m1Forward(int(delay)/1000.0, int(steps))
    #m2Forward(int(delay)/1000.0, int(steps))
    #steps = raw_input("How many steps backwards?")
    #m1Backwards(int(delay)/1000.0, int(steps))
    #m2Backwards(int(delay)/1000.0, int(steps))
