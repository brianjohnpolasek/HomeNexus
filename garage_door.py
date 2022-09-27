import time

import RPi.GPIO as GPIO

# CONSTANTS
door = 12

def pin_setup():
    """Instantiate output pin for garage door"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(door, GPIO.OUT, initial=GPIO.HIGH)

def toggle_garage_door():
    """Sets door output high long enough trip the switch"""
    print("Toggling garage door")
    pin_setup()
    GPIO.output(door, GPIO.LOW)
    time.sleep(1)
    GPIO.output(door, GPIO.HIGH)
    GPIO.cleanup()
