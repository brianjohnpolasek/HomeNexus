import time

import RPi.GPIO as GPIO

# CONSTANTS
master_valve = 18
#valves = [23, 24, 25, 12, 5, 6, 13]
valves = [23, 24, 25, 5, 6, 13]

# PINOUT SETUP
def setup_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(master_valve, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(valves, GPIO.OUT, initial=GPIO.HIGH)

def cleanup_pins():
    GPIO.cleanup()

def run_system(run_time=30):
    """Runs the sprinklers for the provided time"""
    print("Running sprinkler system")
    setup_pins()
    
    GPIO.output(master_valve, GPIO.LOW)
    for valve in valves:
        #toggle_valve(valve, run_time)
        print("Valve " + str(valve))
    GPIO.output(master_valve, GPIO.LOW)
    
    cleanup_pins()
    print("Sprinkler system finished!")


def toggle_valve(valve, run_time):
    """Open valve for desired phase for provided time"""
    print("Running valve " + str(valve))
    GPIO.output(valve, GPIO.LOW)
    time.sleep(run_time)
    GPIO.output(valve, GPIO.HIGH)


if __name__ == "__main__":
    run_system()
