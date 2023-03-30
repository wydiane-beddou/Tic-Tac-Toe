from tkinter import *

import tkinter.messagebox as messagebox

# Définition des constantes pour les joueurs
HUMAN_PLAYER = "X"
AI_PLAYER = "O"
root = Tk()
root.iconbitmap('tic tac toe.ico')
root.title('Tic-Tac-Toe')

# Fonction pour vérifier si le jeu est terminé
def game_over(board):
    # Vérification des lignes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
    # Vérification des colonnes
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return True
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    # Vérification du plateau complet
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
print()

# Fonction pour évaluer le score de la position actuelle
def evaluate(board):
    # Vérification des lignes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == AI_PLAYER:
                return 1
            elif board[i][0] == HUMAN_PLAYER:
                return -1
    # Vérification des colonnes
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == AI_PLAYER:
                return 1
            elif board[0][j] == HUMAN_PLAYER:
                return -1
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == AI_PLAYER:
            return 1
        elif board[0][0] == HUMAN_PLAYER:
            return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == AI_PLAYER:
            return 1
        elif board[0][2] == HUMAN_PLAYER:
            return -1
    # Aucun gagnant
    return 0
print()
# Fonction pour effectuer le mouvement de l'IA
def ai_move(board):
    best_score = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = AI_PLAYER
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = AI_PLAYER
print()
# Fonction Minimax pour l'IA
def minimax(board, is_maximizing):
    if game_over(board):
        return evaluate(board)
    if is_maximizing:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = AI_PLAYER
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
    
# Maximisation de l'IA
        else:
            best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = HUMAN_PLAYER
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
    return best_score
# Si la case est vide et le jeu n'est pas terminé
if board[row][col] == " " and not game_over(board):
    # Joueur humain joue
    board[row][col] = HUMAN_PLAYER
    # Actualisation de l'affichage
    buttons[row][col].configure(text=HUMAN_PLAYER)
    # Vérification si le joueur a gagné
    if game_over(board):
        messagebox.showinfo("Fin de jeu", "Vous avez gagné !")
else:
    # Laisser l'IA jouer
    ai_move(board)
    # Actualisation de l'affichage
    buttons[best_move[0]][best_move[1]].configure(text=AI_PLAYER)
    # Vérification si l'IA a gagné
    if game_over(board):
        messagebox.showinfo("Fin de jeu", "L'IA a gagné !")
