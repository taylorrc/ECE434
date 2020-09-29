#!/bin/bash
#chmod +x

# Temperature sensor needs to be at address 0x48--tie pin 5 low

cd /sys/class/i2c-adapter/i2c-2
#echo tmp101 0x48 > new_device
cd 2-0048/hwmon/hwmon0
cat temp1_input
