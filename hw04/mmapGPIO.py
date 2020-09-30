#!/usr/bin/env python3
#chmod +x
# From: https://graycat.io/tutorials/beaglebone-io-using-python-mmap/
from mmap import mmap
import time, struct

GPIO_OE = 0x134
GPIO0_offset = 0x44E07000
GPIO0_size = 0x44E07FFF-GPIO0_offset

LED0 = 1<<15
LED1 = 1<<17

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset

BUTTON1 = 1<<18
BUTTON0 = 1<<26

GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
GPIO_DATAIN = 0x138


with open("/dev/mem", "r+b" ) as h:
  mem0 = mmap(h.fileno(), GPIO0_size, offset=GPIO0_offset)
with open("/dev/mem", "r+b" ) as f:
  mem1 = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
  
packed_reg0 = mem0[GPIO_OE:GPIO_OE+4]
packed_reg1 = mem1[GPIO_OE:GPIO_OE+4]

reg_status0 = struct.unpack("<L", packed_reg0)[0]
reg_status1 = struct.unpack("<L", packed_reg1)[0]

reg_status0 &= ~(LED0)
reg_status1 &= ~(LED1)


mem0[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status0)
mem1[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status1)

try:
  while(True):
      
    button_packed0 = mem0[GPIO_DATAIN:GPIO_DATAIN+4]
    button_packed1 = mem1[GPIO_DATAIN:GPIO_DATAIN+4] 
    
    button_unpacked0 = struct.unpack("<L", button_packed0)[0]
    button_unpacked1 = struct.unpack("<L", button_packed1)[0]
    
    if((button_unpacked0 & BUTTON0) == BUTTON0):
        mem0[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED0)
    else:
        mem0[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED0)

    if((button_unpacked1 & BUTTON1) == BUTTON1):
        mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED1)
    else:
        mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED1)

    # mem0[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED0)
    # mem0[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", LED1)

    # time.sleep(0.5)
    # mem0[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED0)
    # mem0[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", LED1)

    time.sleep(0.5)

except KeyboardInterrupt:
  mem0.close()



