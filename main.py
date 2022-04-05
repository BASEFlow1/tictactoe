import os
import random as rand
import time
from sys import exit
from shutil import get_terminal_size
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def split(word):
    return [char for char in word]

def drawBoard():
    columns = get_terminal_size().columns
    lines = get_terminal_size().lines
    brett = []
    for x in board:
        for y in x:
            if y == 0:
                brett.append('-')
            elif y == 1:
                brett.append('X')
            elif y == 2:
                brett.append('O')
        print("\n", end = "")    

    for x in range(int(lines / 4) - 3):
        print("")
    print("+---+---+---+".center(columns), end = '')
    print(f"| {brett[0]} | {brett[1]} | {brett[2]} |".center(columns), end = '')
    print("+---+---+---+".center(columns), end = '')
    print(f"| {brett[3]} | {brett[4]} | {brett[5]} |".center(columns), end = '')
    print("+---+---+---+".center(columns), end = '')
    print(f"| {brett[6]} | {brett[7]} | {brett[8]} |".center(columns), end = '')
    print("+---+---+---+".center(columns), end = '')

def manipulateBoard(row, column, replacement):
    board[row][column] = replacement

def moveCharConversion(x):
    if x == 1:
        return "X"
    elif x == 2:
        return "O"
    else:
        return "NULL"

def rowColumnConversion(play):
    if play <= 9:
        if play == 1:
            return [0, 0]
        elif play == 2:
            return [0, 1]
        elif play == 3:
            return [0, 2]
        elif play == 4:
            return [1, 0]
        elif play == 5:
            return [1, 1]
        elif play == 6:
            return [1, 2]
        elif play == 7:
            return [2, 0]
        elif play == 8:
            return [2, 1]
        elif play == 9:
            return [2, 2]

def checkForWin():
    winCombinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in winCombinations:
        isWinning = 0
        for y in x:
            temp = rowColumnConversion(y)
            if board[temp[0]][temp[1]] != 0 and board[temp[0]][temp[1]] != currentMove:
                isWinning += 1
            else:
                break
        if isWinning >= 3:
            return True
    return False

def checkForDraw():
    if round >= 9:
        return True
    else:
        return False

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
currentMove = rand.randrange(1, 3)
round = 1
doGuide = False

if doGuide:
    columns = get_terminal_size().columns
    print("+---+---+---+".center(columns), end = '')
    print(f"| 1 | 2 | 3 |".center(columns), end = '')
    print("+---+---+---+".center(columns), end = '')
    print(f"| 4 | 5 | 6 |".center(columns), end = '')
    print("+---+---+---+".center(columns), end = '')
    print(f"| 7 | 8 | 9 |".center(columns), end = '')
    print("+---+---+---+".center(columns), end = '')
    time.sleep(5)
    clearConsole()

while True:
    while True:
        clearConsole()
        columns = get_terminal_size().columns
        drawBoard()
        print(f"It's {moveCharConversion(currentMove)}'s turn!".center(columns), end = '')
        print(f"Round {round}".center(columns), end = '')
        try:
            play = int(input("Pick your play: "))
        except:
            print("Invalid.".center(columns))
            break
        play = rowColumnConversion(play)
        manipulateBoard(play[0], play[1], currentMove)
        if checkForWin():
            clearConsole()
            drawBoard()
            print(f"{moveCharConversion(currentMove)} won!".center(columns), end = '')
            exit()
        if checkForDraw():
            clearConsole()
            drawBoard()
            print(f"Draw!".center(columns), end = '')
            exit()
        currentMove = 2 if currentMove == 1 else 1
        round += 1