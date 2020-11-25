import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import constant

GPIO.setup(constant.RED, GPIO.OUT)
GPIO.setup(constant.GREEN, GPIO.OUT)
GPIO.setup(constant.BLUE, GPIO.OUT)

RED = GPIO.PWM(constant.RED, constant.FREQ)
GREEN = GPIO.PWM(constant.GREEN, constant.FREQ)
BLUE = GPIO.PWM(constant.BLUE, constant.FREQ)

RUNNING = True

try:
    RED.start(0)
    GREEN.start(0)
    BLUE.start(0)
    while RUNNING:
        # Lighting up the RGB led. 100 means giving 100% to the pin
        for x in range(101):
            GREEN.ChangeDutyCycle(x)  # Changes the width of the PWM duty cycle
            time.sleep(0.05)
        for x in range(101):
            RED.ChangeDutyCycle(100 - x)
            time.sleep(0.025)
        for x in range(101):
            GREEN.ChangeDutyCycle(100 - x)
            BLUE.ChangeDutyCycle(x)
            time.sleep(0.025)
        for x in range(101):
            RED.ChangeDutyCycle(x)
            time.sleep(0.025)
except KeyboardInterrupt:
    # Gracefully exit the RGB lighting loop in order to shut down the lights
    RUNNING = False
    GPIO.cleanup()