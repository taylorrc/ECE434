#!/usr/bin/env python3
#chmod +x

import numpy
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

# Setting up all button inputs
upButton = "P9_42"
downButton = "P9_41"
leftButton = "P9_26"
rightButton = "P9_23"
shakeButton = "P9_27"
exitButton = "P9_30"

# Adding event detection to each button
GPIO.setup(upButton, GPIO.IN)
GPIO.add_event_detect(upButton, GPIO.RISING)

GPIO.setup(downButton, GPIO.IN)
GPIO.add_event_detect(downButton, GPIO.RISING)

GPIO.setup(leftButton, GPIO.IN)
GPIO.add_event_detect(leftButton, GPIO.RISING)

GPIO.setup(rightButton, GPIO.IN)
GPIO.add_event_detect(rightButton, GPIO.RISING)

GPIO.setup(shakeButton, GPIO.IN)
GPIO.add_event_detect(shakeButton, GPIO.RISING)

GPIO.setup(exitButton, GPIO.IN)
GPIO.add_event_detect(exitButton, GPIO.RISING)


# Printing the instructions
print("Welcome to Etch-A-Sketch!")
print("Commands to use:")
print("1. Up--Move cursor up")
print("2. Down--Move cursor down")
print("3. Left--Move cursor left")
print("4. Right--Move cursor right")
print("5. Shake--clear the gameboard")
print("6. Exit--exit the game")
print("Have fun!")
print(" ")

# Reading Coordinates
# boardHeight = 1 + int(input("Height of Board? "))
# boardLength = 1 + int(input("Length of Board? "))
boardHeight = 8;
boardLength = 8;

# Generating the gameboard
gameBoard = numpy.full((boardHeight + 1, boardLength), ' ')
lightBoard = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

# Putting numbers on the top and left side of the board
# for i in range(boardLength):
#     gameBoard[0][i] = i

# for i in range(boardHeight):
#     gameBoard[i][0] = i

# Setting up the cursor
cursorX = 0
cursorY = 1
gameBoard[cursorY][cursorX] = '|'
lightBoard[2*cursorX + 1] = (1 << (8-cursorY))

# Printing the initial gameboard
print(gameBoard)
bus.write_i2c_block_data(matrix, 0, lightBoard)


# Main game loop
while(1):
    # All player moves are determined by button presses
    
    # Reading going Right
    if GPIO.event_detected(rightButton):

        # Checking Boundaries
        if(cursorX >= boardLength - 1):
            print("Cannot go Right!")
        
        # Moving cursor and printing
        else: 
            
            gameBoard[cursorY][cursorX] = 'x'
            lightBoard[2*cursorX + 1] = lightBoard[2*cursorX + 1] | (1 << (8-cursorY))

            cursorX+=1
            gameBoard[cursorY][cursorX] = '|'
            # lightBoard[2*cursorX - 2] = (1 << (8-cursorY))

            print(gameBoard)
            bus.write_i2c_block_data(matrix, 0, lightBoard)
            print("RIGHT")
            
            print("X: ", cursorX)
            print("Y: ", cursorY)


    # Reading going Left
    if GPIO.event_detected(leftButton):


        # Checking Boundaries
        if(cursorX <= 0):
            print("Cannot go Left!")
        
        # Moving cursor and printing
        else: 

            
            gameBoard[cursorY][cursorX] = 'x'
            lightBoard[2*cursorX + 1] =lightBoard[2*cursorX + 1] | (1 << (8-cursorY))


            cursorX-=1
            gameBoard[cursorY][cursorX] = '|'
            # lightBoard[2*cursorX - 2] = (1 << (8-cursorY))

            print(gameBoard)
            bus.write_i2c_block_data(matrix, 0, lightBoard)
            print("LEFT")
            
            print("X: ", cursorX)
            print("Y: ", cursorY)


    # Reading going Up
    if GPIO.event_detected(upButton):

        # Checking Boundaries
        if(cursorY <= 0 + 1):
            print("Cannot go Up!")
        
        # Moving cursor and printing
        else: 

            
            gameBoard[cursorY][cursorX] = 'x'
            lightBoard[2*cursorX + 1] = lightBoard[2*cursorX + 1] | (1 << (8-cursorY))

            cursorY-=1
            gameBoard[cursorY][cursorX] = '|'
            # lightBoard[2*cursorX - 2] = (1 << (8-cursorY))

            print(gameBoard)
            bus.write_i2c_block_data(matrix, 0, lightBoard)
            print("UP")
            
            print("X: ", cursorX)
            print("Y: ", cursorY)


    # Reading going Down
    if GPIO.event_detected(downButton):

        # Checking Boundaries
        if(cursorY >= boardHeight - 1 + 1):
            print("Cannot go Down!")
        
        # Moving cursor and printing
        else: 

            gameBoard[cursorY][cursorX] = 'x'
            lightBoard[2*cursorX + 1] = lightBoard[2*cursorX + 1] | (1 << (8-cursorY))

            cursorY+=1
            gameBoard[cursorY][cursorX] = '|'
            # lightBoard[2*cursorX - 2] = (1 << (8-cursorY))

            print(gameBoard)
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

        # Putting Numbers back on top and side
        # for i in range(boardLength):
        #     gameBoard[0][i] = i

        # for i in range(boardHeight):
        #     gameBoard[i][0] = i
            
        
        lightBoard = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        ]

        # Putting back the cursor
        cursorX = 0
        cursorY = 1
        gameBoard[cursorY][cursorX] = '|'

        # Printing gameboard
        print("X: ", cursorX)
        print("Y: ", cursorY)
        
        print(gameBoard)
        bus.write_i2c_block_data(matrix, 0, lightBoard)

        print("SHAKE")

    # Reading Exit Command
    if GPIO.event_detected(exitButton):
        print("Exiting...")
        break


