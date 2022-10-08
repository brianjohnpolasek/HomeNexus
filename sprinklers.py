import time

import RPi.GPIO as GPIO

# CONSTANTS
MASTER_VALVE = 18
#VALVES = [23, 24, 25, 12, 5, 6, 13]
VALVES = [23, 24, 25, 5, 6, 13]
DEFAULT_RUNTIME = 60

# PINOUT SETUP
def setup_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(MASTER_VALVE, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(VALVES, GPIO.OUT, initial=GPIO.HIGH)

def cleanup_pins():
    GPIO.cleanup()

def run_system(run_time=DEFAULT_RUNTIME):
    """Runs the sprinklers for the provided time"""
    print("Running sprinkler system")
    setup_pins()
    
    GPIO.output(MASTER_VALVE, GPIO.LOW)
    for valve in VALVES:
        #toggle_valve(valve, run_time)
        print("Valve " + str(valve))
    GPIO.output(MASTER_VALVE, GPIO.LOW)
    
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
