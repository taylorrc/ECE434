#!/usr/bin/env python3
#chmod +x

import numpy
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
import blynklib
import blynktimer
import os

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
# create timers dispatcher instance
timer = blynktimer.Timer()

# Configuring 8x8 Matrix
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# Printing the instructions
print("Welcome to Etch-A-Sketch!")
print("Have fun!")
print(" ")

# Reading Coordinates
boardHeight = 8
boardLength = 8

# Generating the gameboard
gameBoard = numpy.full((boardHeight + 1, boardLength), ' ')
lightBoard = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

# Setting up the cursor -- y starts at 1 to accommodate for led matrix
cursorX = 0
cursorY = 1
gameBoard[cursorY][cursorX] = '|'
lightBoard[2*cursorX] = (1 << (8-cursorY))

# Printing the initial gameboard
print(gameBoard)
bus.write_i2c_block_data(matrix, 0, lightBoard)

# Handling going up
@blynk.handle_event('write V0')
def my_write_handler(pin, value):

    global boardHeight
    global boardLength
    global gameBoard
    global lightBoard
    global cursorX
    global cursorY    
    
    print('Current V{} value: {}'.format(pin, value))
    # GPIO.output(LED, int(value[0]))
    print("Up pressed")
    
    # Checking Boundaries
    if(cursorY <= 0 + 1):
        print("Cannot go Up!")
    
    # Moving cursor and printing
    else: 

        gameBoard[cursorY][cursorX] = 'x'
        lightBoard[2*cursorX + 1] = lightBoard[2*cursorX + 1] | (1 << (8-cursorY))

        cursorY-=1
        gameBoard[cursorY][cursorX] = '|'
        for k in range(0, 16, 2):
            lightBoard[k] = 0x00
        lightBoard[2*cursorX] = (1 << (8-cursorY))

        bus.write_i2c_block_data(matrix, 0, lightBoard)
        print("UP")
        
        print("X: ", cursorX)
        print("Y: ", cursorY)
    
# Handling going Right
@blynk.handle_event('write V1')
def move_right(pin, value):
    
    global boardHeight
    global boardLength
    global gameBoard
    global lightBoard
    global cursorX
    global cursorY
    
    print('Current V{} value: {}'.format(pin, value))
    # GPIO.output(LED, int(value[0]))
    print("Right pressed")

    # Checking Boundaries
    if(cursorX >= boardLength - 1):
        print("Cannot go Right!")
    
    # Moving cursor and printing
    else: 
        print("going Right")
        # Marking out in red where the player has been previously
        gameBoard[cursorY][cursorX] = 'x'
        lightBoard[2*cursorX + 1] = lightBoard[2*cursorX + 1] | (1 << (8-cursorY))

        # Moving the cursor
        cursorX+=1
        gameBoard[cursorY][cursorX] = '|'
        
        # Clearing all green from the board and setting the cursor
        for k in range(0, 16, 2):
            lightBoard[k] = 0x00
        lightBoard[2*cursorX] = (1 << (8-cursorY))
        
        
        # Printing the gameboard
        bus.write_i2c_block_data(matrix, 0, lightBoard)
        print("RIGHT")
        print("X: ", cursorX)
        print("Y: ", cursorY)

# Handling going Left
@blynk.handle_event('write V2')
def my_write_handler(pin, value):
    
    global boardHeight
    global boardLength
    global gameBoard
    global lightBoard
    global cursorX
    global cursorY
    
    print('Current V{} value: {}'.format(pin, value))
    # GPIO.output(LED, int(value[0]))
    print("Left pressed")
    
    # Checking Boundaries
    if(cursorX <= 0):
        print("Cannot go Left!")

    # Moving cursor and printing
    else: 
    
        gameBoard[cursorY][cursorX] = 'x'
        lightBoard[2*cursorX + 1] =lightBoard[2*cursorX + 1] | (1 << (8-cursorY))

        cursorX-=1
        gameBoard[cursorY][cursorX] = '|'
        for k in range(0, 16, 2):
            lightBoard[k] = 0x00
        lightBoard[2*cursorX] = (1 << (8-cursorY))

        bus.write_i2c_block_data(matrix, 0, lightBoard)
        print("LEFT")
    
        print("X: ", cursorX)
        print("Y: ", cursorY)
    
# Handling going Down
@blynk.handle_event('write V3')
def my_write_handler(pin, value):
    
    global boardHeight
    global boardLength
    global gameBoard
    global lightBoard
    global cursorX
    global cursorY
    
    print('Current V{} value: {}'.format(pin, value))
    # GPIO.output(LED, int(value[0]))
    print("Down pressed")
    
    # Checking Boundaries
    if(cursorY >= boardHeight - 1 + 1):
        print("Cannot go Down!")
    
    # Moving cursor and printing
    else: 

        gameBoard[cursorY][cursorX] = 'x'
        lightBoard[2*cursorX + 1] = lightBoard[2*cursorX + 1] | (1 << (8-cursorY))

        cursorY+=1
        gameBoard[cursorY][cursorX] = '|'
        for k in range(0, 16, 2):
            lightBoard[k] = 0x00
        lightBoard[2*cursorX] = (1 << (8-cursorY))

        bus.write_i2c_block_data(matrix, 0, lightBoard)
        print("DOWN")

        print("X: ", cursorX)
        print("Y: ", cursorY)
        
# Handling Shake
@blynk.handle_event('write V4')
def my_write_handler(pin, value):
    
    global boardHeight
    global boardLength
    global gameBoard
    global lightBoard
    global cursorX
    global cursorY
    
    # Nulling out all characters
    for i in range(boardLength):
        for k in range(boardHeight + 1):
            gameBoard[k][i] = ' '

    lightBoard = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ]

    # Putting back the cursor
    cursorX = 0
    cursorY = 1
    gameBoard[cursorY][cursorX] = '|'
    lightBoard[2*cursorX] = (1 << (8-cursorY))

    # Printing gameboard
    print("X: ", cursorX)
    print("Y: ", cursorY)
    bus.write_i2c_block_data(matrix, 0, lightBoard)

    print("SHAKE")
    
while True:
    blynk.run()
    time.sleep(0.1)