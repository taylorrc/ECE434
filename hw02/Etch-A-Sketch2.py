#!/usr/bin/env python3
#chmod +x

import numpy
import Adafruit_BBIO.GPIO as GPIO

# Setting up all button inputs
upButton = "P9_42"
downButton = "P9_23"
leftButton = "P9_20"
rightButton = "P9_14"
shakeButton = "P9_16"
exitButton = "P9_18"

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
boardHeight = 1 + int(input("Height of Board? "))
boardLength = 1 + int(input("Length of Board? "))

# Generating the gameboard
gameBoard = numpy.full((boardHeight, boardLength), ' ')

# Putting numbers on the top and left side of the board
for i in range(boardLength):
    gameBoard[0][i] = i

for i in range(boardHeight):
    gameBoard[i][0] = i

# Setting up the cursor
cursorX = 1
cursorY = 1
gameBoard[cursorY][cursorX] = '|'

# Printing the initial gameboard
print(gameBoard)

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

            cursorX+=1
            gameBoard[cursorY][cursorX] = '|'

            print(gameBoard)
            print("RIGHT")


    # Reading going Left
    if GPIO.event_detected(leftButton):


        # Checking Boundaries
        if(cursorX <= 1):
            print("Cannot go Left!")
        
        # Moving cursor and printing
        else: 
            gameBoard[cursorY][cursorX] = 'x'

            cursorX-=1
            gameBoard[cursorY][cursorX] = '|'

            print(gameBoard)
            print("LEFT")


    # Reading going Up
    if GPIO.event_detected(upButton):

        # Checking Boundaries
        if(cursorY <= 1):
            print("Cannot go Up!")
        
        # Moving cursor and printing
        else: 
            gameBoard[cursorY][cursorX] = 'x'

            cursorY-=1
            gameBoard[cursorY][cursorX] = '|'

            print(gameBoard)
            print("UP")


    # Reading going Down
    if GPIO.event_detected(downButton):

        # Checking Boundaries
        if(cursorY >= boardHeight - 1):
            print("Cannot go Down!")
        
        # Moving cursor and printing
        else: 
            gameBoard[cursorY][cursorX] = 'x'

            cursorY+=1
            gameBoard[cursorY][cursorX] = '|'

            print(gameBoard)
            print("DOWN")


    # Reading Shake 
    if GPIO.event_detected(shakeButton):
 
        # Nulling out all characters
        for i in range(boardLength):
            for k in range(boardHeight):
                gameBoard[k][i] = ' '

        # Putting Numbers back on top and side
        for i in range(boardLength):
            gameBoard[0][i] = i

        for i in range(boardHeight):
            gameBoard[i][0] = i

        # Putting back the cursor
        cursorX = 1
        cursorY = 1
        gameBoard[cursorY][cursorX] = '|'

        # Printing gameboard
        print(gameBoard)
        print("SHAKE")

    # Reading Exit Command
    if GPIO.event_detected(exitButton):
        print("Exiting...")
        break


