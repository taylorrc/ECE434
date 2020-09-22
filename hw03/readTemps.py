#!/usr/bin/env python3
#chmod +x

import smbus

bus = smbus.SMBus(2)  # Use i2c bus 1
tempSens1 = 0x48         # Use address 0x70
tempSens2 = 0x4a         # Use address 0x70

val1 = bus.read_byte_data(tempSens1, 0)
val2 = bus.read_byte_data(tempSens2, 0)

output1 = ((9/5)*val1) + 32
output2 = ((9/5)*val2) + 32

print("Temp 1:", output1)
print("Temp 2:", output2)