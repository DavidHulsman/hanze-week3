import constant
import RPi.GPIO as GPIO
import time
import hue_to_rgb_led

GPIO.setmode(GPIO.BCM)

GPIO.setup(constant.RED, GPIO.OUT)
GPIO.setup(constant.GREEN, GPIO.OUT)
GPIO.setup(constant.BLUE, GPIO.OUT)

RED = GPIO.PWM(constant.RED, constant.FREQ)
GREEN = GPIO.PWM(constant.GREEN, constant.FREQ)
BLUE = GPIO.PWM(constant.BLUE, constant.FREQ)

RED.start(0)
GREEN.start(0)
BLUE.start(0)

running = True

try:
    RED.start(0)
    GREEN.start(0)
    BLUE.start(0)
    while running:
        # Lighting up the RGB led for 360 steps
        for x in range(361):
            r, g, b = hue_to_rgb_led(x / 360)
            RED.ChangeDutyCycle(r)
            GREEN.ChangeDutyCycle(g)
            BLUE.ChangeDutyCycle(b)
            time.sleep(1)

except KeyboardInterrupt:
    running = False
    GPIO.cleanup()
