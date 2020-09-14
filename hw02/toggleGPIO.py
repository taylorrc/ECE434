#!/usr/bin/python3
#chmod +x

import Adafruit_BBIO.GPIO as GPIO
import time

out = "P9_12"
period = 0.005
 
GPIO.setup(out, GPIO.OUT)
 
while True:
    GPIO.output(out, GPIO.HIGH)
    time.sleep(period/2)
    GPIO.output(out, GPIO.LOW)
    time.sleep(period/2)