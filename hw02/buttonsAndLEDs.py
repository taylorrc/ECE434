#!/usr/bin/env python3
#chmod +x

import Adafruit_BBIO.GPIO as GPIO

# Setting up all button inputs
upButton = "P9_42"
downButton = "P9_23"
leftButton = "P9_20"
rightButton = "P9_14"

# Setting up all LED outputs
upLED = "P9_27"
downLED = "P9_21"
leftLED = "P9_17"
rightLED = "P9_12"

# Adding event detection to each button
GPIO.setup(upButton, GPIO.IN)
GPIO.add_event_detect(upButton, GPIO.RISING)

GPIO.setup(downButton, GPIO.IN)
GPIO.add_event_detect(downButton, GPIO.RISING)

GPIO.setup(leftButton, GPIO.IN)
GPIO.add_event_detect(leftButton, GPIO.RISING)

GPIO.setup(rightButton, GPIO.IN)
GPIO.add_event_detect(rightButton, GPIO.RISING)

# Setting up LED outputs
GPIO.setup(upLED, GPIO.OUT)
GPIO.setup(downLED, GPIO.OUT)
GPIO.setup(leftLED, GPIO.OUT)
GPIO.setup(rightLED, GPIO.OUT)

upNum = 0
downNum = 0
leftNum = 0
rightNum = 0

while True:
    if GPIO.event_detected(upButton):
        if(upNum % 2 == 0):
            GPIO.output(upLED, GPIO.HIGH)
        else:
            GPIO.output(upLED, GPIO.LOW)
        upNum+=1
        
        
    if GPIO.event_detected(downButton):
        if(downNum % 2 == 0):
            GPIO.output(downLED, GPIO.HIGH)
        else:
            GPIO.output(downLED, GPIO.LOW)
        downNum+=1
        
    if GPIO.event_detected(leftButton):
        if(leftNum % 2 == 0):
            GPIO.output(leftLED, GPIO.HIGH)
        else:
            GPIO.output(leftLED, GPIO.LOW)
        leftNum+=1
        
    if GPIO.event_detected(rightButton):
        if(rightNum % 2 == 0):
            GPIO.output(rightLED, GPIO.HIGH)
        else:
            GPIO.output(rightLED, GPIO.LOW)
        rightNum+=1

