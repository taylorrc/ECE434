#!/usr/bin/env python3
#chmod +x

import numpy

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
    userInput = input("Next move? ")

    # Reading going Right
    if(userInput == "Right" or userInput == "right"):

        # Checking Boundaries
        if(cursorX >= boardLength - 1):
            print("Cannot go Right!")
        
        # Moving cursor and printing
        else: 
            gameBoard[cursorY][cursorX] = 'x'

            cursorX+=1
            gameBoard[cursorY][cursorX] = '|'

            print(gameBoard)


    # Reading going Left
    if(userInput == "Left" or userInput == "left"):

        # Checking Boundaries
        if(cursorX <= 1):
            print("Cannot go Left!")
        
        # Moving cursor and printing
        else: 
            gameBoard[cursorY][cursorX] = 'x'

            cursorX-=1
            gameBoard[cursorY][cursorX] = '|'

            print(gameBoard)


    # Reading going Up
    if(userInput == "Up" or userInput == "up"):

        # Checking Boundaries
        if(cursorY <= 1):
            print("Cannot go Up!")
        
        # Moving cursor and printing
        else: 
            gameBoard[cursorY][cursorX] = 'x'

            cursorY-=1
            gameBoard[cursorY][cursorX] = '|'

            print(gameBoard)


    # Reading going Down
    if(userInput == "Down" or userInput == "down"):

        # Checking Boundaries
        if(cursorY >= boardHeight - 1):
            print("Cannot go Down!")
        
        # Moving cursor and printing
        else: 
            gameBoard[cursorY][cursorX] = 'x'

            cursorY+=1
            gameBoard[cursorY][cursorX] = '|'

            print(gameBoard)


    # Reading Shake 
    if(userInput == "Shake" or userInput == "shake"):
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

    # Reading Exit Command
    if(userInput == "Exit" or userInput == "exit"):
        break


