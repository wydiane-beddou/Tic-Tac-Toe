from tkinter import *
from tkinter import messagebox
import random
import tkinter as tk

# Définition du plateau
root = tk.Tk()
root.geometry("300x200")
root.iconbitmap('tic tac toe.ico')
root.title('Tic Tac Toe by Wydiane')

player = 'O'
bot = 'X'


def printBoard(board):
    print(board[1]+ '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4]+ '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7]+ '|' + board[8] + '|' + board[9])
    print('\n')

printBoard(board)

def spaceIsFree(position):
    if(board[position] == ' '):
        return True
    else:
        return False 
    
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
    
def checkWichSigneWon(signe):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == signe):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == signe):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == signe):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == signe):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == signe):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == signe):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == signe):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == signe):
        return True
    else:
        return False


def insertLetter(letter, position):

    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if(checkDraw()):
            print("Draw!")
            exit()

        if checkForWin():
            if letter == 'X':
                print("Bot wins !")
            else:
                print("Player wins !")
                exit()
        return
    
    else:
        print("Can't insert there !")
        position = int(input("Enter new position : "))
        insertLetter(letter,position)
        return
    



def playerMove():
    position = int(input("Enter the position for 'O':"))
    insertLetter(player, position)
    return

def iaMove():
    bestScore= -1000
    bestMove = 0
    
    for key in board.keys():
        if (board[key]== ' '):
            board[key] = botscore = minimax(board,0,False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score 
                bestMove = key
                
    insertLetter(bot,bestMove)
    return


def minimax(board, depth, isMaximizing):
    
    if checkWichSigneWon(bot):
        return 100
    
    elif checkWichSigneWon(player):
        return -100
    
    elif checkDraw():
        return 0
    
    if isMaximizing:
        bestScore= -1000
        for key in board.keys():
            if (board[key]== ' '):
                score = minimax(board,0,False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score 
    else:
        bestScore = 1000
        for key in board.keys():
            if (board[key]== ' '):
                board[key] = player 
                score = minimax(board, 0, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score 
    return bestScore

while not checkForWin():
    iaMove()
    playerMove()
      

root.mainloop()