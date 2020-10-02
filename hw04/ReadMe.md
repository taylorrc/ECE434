# hw04 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Memory map 
|  4 | mmap()
|  4 | i2c via Kernel
|  4 | Etch-a-Sketch via flask
|  4 | LCD display
|  1 | Extras
| 19 | **Total**

*My comments are in italics. --may*

*looks good.  Nice set of pictures.*

# ECE434 HW04 
# Ryan Taylor

## Memory Map
I created a memory map diagram for the beaglebone and submitted it as a .pdf called "mmapOfBeagle.pdf"

## GPIO via mmap
1. I created a file called "mmapGPIO.py" that reads from 2 button inputs and controls two LEDs using mmap commands. 
2. I modified toggleLED.py as an example document and took out the usleeps at the end of the loop. 

GPIO with mmap using python: 11.9uS period without any sleeps
This is faster than toggling in python as we did in homework 2, but not faster than the fastest toggle time written in c. I would be curious to see if an mmap file written in c would have better toggle speeds.

*I think it is*

## I2C via the Kernel Driver
1. I made a shell script called "i2cTempRead.sh" which follows some of the same commands used in the example document. The temperature of the TMP101 sensor is output in milli-degrees celcius. 

## Control the LED matrix from a browser
I modified my etch-a-sketch program to be compatible with a web browser via flask. The webpage can be found at 192.168.7.1:8081 in a browser.

## 2.4" TFT LCD Display
All of the pictures I took from working with the LCD display are in a folder titled "hw04Pictures"

I was able to display an image of Boris and rotate it, play "Reds nightmare" and rotate it, and generate text and display it on the LCD. 
