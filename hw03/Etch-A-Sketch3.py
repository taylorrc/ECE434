#!/usr/bin/env python3
#chmod +x

import numpy
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import smbus
import time

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

# Setting up both encoders
rlEncoder = RotaryEncoder(eQEP1)
rlEncoder.setAbsolute()

udEncoder = RotaryEncoder(eQEP2)
udEncoder.setAbsolute()

# Configuring 8x8 Matrix
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# Setting up all button inputs
shakeButton = "P9_27"
exitButton = "P9_30"

# Adding event detection to each button
GPIO.setup(shakeButton, GPIO.IN)
GPIO.add_event_detect(shakeButton, GPIO.RISING)

GPIO.setup(exitButton, GPIO.IN)
GPIO.add_event_detect(exitButton, GPIO.RISING)


# Printing the instructions
print("Welcome to Etch-A-Sketch!")
print("Have fun!")
print(" ")

# Reading Coordinates
boardHeight = 8;
boardLength = 8;

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

# Setting the initial positions of the encoders
rlold_pos = rlEncoder.position
udold_pos = udEncoder.position

# Main game loop
while(1):
    # All player moves are determined by rotary encoders
    rlcur_pos = rlEncoder.position
    udcur_pos = udEncoder.position
    
    # Reading going Right -- All other movement buttons follow same code structure
    if rlcur_pos > rlold_pos:

        # Checking Boundaries
        if(cursorX >= boardLength - 1):
            print("Cannot go Right!")
        
        # Moving cursor and printing
        else: 
            
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


    # Reading going Left
    if rlcur_pos < rlold_pos:


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


    # Reading going Up
    if udcur_pos > udold_pos:

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


    # Reading going Down
    if udcur_pos < udold_pos:

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

    # Reading Shake 
    if GPIO.event_detected(shakeButton):
 
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

    # Reading Exit Command
    if GPIO.event_detected(exitButton):
        print("Exiting...")
        break
    
    # Setting old values as current values
    rlold_pos = rlcur_pos
    udold_pos = udcur_pos
    
    # Sleeping to avoid erraneous behavior
    time.sleep(0.1)


