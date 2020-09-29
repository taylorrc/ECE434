#!/usr/bin/env python3
#chmod +x

import numpy
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
from flask import Flask, render_template, request
app = Flask(__name__)

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

# Configuring 8x8 Matrix
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

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

@app.route("/")
def index():
	# Read Sensors Status
	ledRedSts = 0
	templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : ledRedSts,
        }
	return render_template('index4.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	
    global boardHeight
    global boardLength
    global gameBoard
    global lightBoard
    global cursorX
    global cursorY
    ledRedSts = 0
	
	#Checking which Button Had been pressed
    if deviceName == 'rightButton':
		
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
            
    if deviceName == 'leftButton':
        
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
        
    if deviceName == 'upButton':
        
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
        
    if deviceName == 'downButton':
        
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
        
    if deviceName == 'shakeButton':
        
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

    if deviceName == 'exitButton':
        print("Exiting...")
        
    templateData = {
          'ledRed'  : ledRedSts,
    }	     

    return render_template('index4.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
