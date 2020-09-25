# hw03 grading

| Points      | Description |
| ----------- | ----------- |
|  5 | TMP101 
|  3 |   | setup.sh
|  2 |   | Documentation
|  5 | Etch-a-Sketch
|  3 |   | setup.sh
|  2 |   | Documentation
| 20 | **Total**

*My comments are in italics. --may*

# ECE434 Homework 3
# Ryan Taylor

## TMP101
On TI.com, I found the datasheet for the TMP101 temperature sensor and found the pinout for the SCL and SDA pins. From the datasheet, I found that if the ADD0 pin of the sensor is grounded, the I2C address of the device is 0x48 and if it is tied to power the address is 0x4a. 

Included in my homework folder is ./tempSetup.sh which sets the high and low temperature cutoffs for each of the tmp101 sensors. 

./readTemps.py and ./readTemps.sh read the temperatures of the tmp101 sensors through the I2C bus in degrees Farenheit.

./tempLimit.py waits for an interrupt on the ALERT pin of each of the sensors, and when the interrupt occurs the program prints the temperature value of each of the sensors in Farenheit.

## Etch-a-sketch
I modified the ./Etch-A-Sketch3.py to include the 8x8 LED Matrix and two rotary encoders instead of pushbuttons. The LED matrix is controlled using the I2C interface and the rotary encoders are controlled through eqep. 
./setup.sh configures the pins for the rotary encoders. 

