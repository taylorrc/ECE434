#!/usr/bin/env python3
# Blink read the temperature from a TMP101 and display it
import blynklib
import blynktimer
import os
import smbus

bus = smbus.SMBus(2)  # Use i2c bus 1
tempSens1 = 0x48         # Use address 0x70

# Run setup.sh to create a new TMP101
TMP101='/sys/class/i2c-adapter/i2c-2/2-0077/iio:device1/in_temp_input'

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
# create timers dispatcher instance
timer = blynktimer.Timer()

# Register Virtual Pins
# The V* says to response to all virtual pins
@blynk.handle_event('write V*')
def my_write_handler(pin, value):
    print('Current V{} value: {}'.format(pin, value))
    GPIO.output(LED, int(value[0])) 

oldtemp = 0
# Code below: register a timer for different pins with different intervals
# run_once flag allows to run timers once or periodically
@timer.register(vpin_num=10, interval=0.5, run_once=False)
def write_to_virtual_pin(vpin_num=1):
    global oldtemp
    # # Open the file with the temperature
    # f = open(TMP101, "r")
    # temp=f.read()[:-1]     # Remove trailing new line
    # # Convert from mC to C
    # temp = int(temp)/1000
    # f.close()
    
    val1 = bus.read_byte_data(tempSens1, 0)
    temp1 = ((9/5)*val1) + 32

    # Only display if changed
    if(temp1 != oldtemp):
        print("Pin: V{} = '{}".format(vpin_num, str(temp1)))
        # Send to blynk
        blynk.virtual_write(vpin_num, temp1)
        oldtemp = temp1

while True:
    blynk.run()
    timer.run()
