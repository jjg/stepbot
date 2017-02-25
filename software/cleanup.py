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

GPIO.cleanup([coil_A_1_pin, coil_A_2_pin, coil_B_1_pin, coil_B_2_pin, coil_C_1_pin, coil_C_2_pin, coil_D_1_pin,coil_D_2_pin])
