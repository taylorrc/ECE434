#!/usr/bin/env python3
#chmod +x

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

# Setting up I2C communication for temp sensors
bus = smbus.SMBus(2)  # Use i2c bus 1
tempSens1 = 0x48         # Use address 0x70
tempSens2 = 0x4a         # Use address 0x70

# Setting up inputs from alert pins
alertOne = "P9_41"
alertTwo = "P9_42"

# Adding event detection to alert pins
GPIO.setup(alertOne, GPIO.IN)
GPIO.add_event_detect(alertOne, GPIO.FALLING)

GPIO.setup(alertTwo, GPIO.IN)
GPIO.add_event_detect(alertTwo, GPIO.FALLING)

# Main loop waiting for temp alert
while(1):
    if GPIO.event_detected(alertOne):
        val1 = bus.read_byte_data(tempSens1, 0)
        val2 = bus.read_byte_data(tempSens2, 0)
        
        output1 = ((9/5)*val1) + 32
        output2 = ((9/5)*val2) + 32
        
        print("Temp 1:", output1)
        print("Temp 2:", output2)
        
    if GPIO.event_detected(alertTwo):
        val1 = bus.read_byte_data(tempSens1, 0)
        val2 = bus.read_byte_data(tempSens2, 0)
        
        output1 = ((9/5)*val1) + 32
        output2 = ((9/5)*val2) + 32
        
        print("Temp 1:", output1)
        print("Temp 2:", output2)
        
    time.sleep(0.1)