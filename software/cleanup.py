import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

coil_A_1_pin = 24
coil_A_2_pin = 16
coil_B_1_pin = 18
coil_B_2_pin = 22

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

GPIO.cleanup([coil_A_1_pin, coil_A_2_pin, coil_B_1_pin, coil_B_2_pin])
