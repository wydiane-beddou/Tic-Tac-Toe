from tkinter import *
from tkinter import messagebox
import random
from tkinter import Canvas
root = Tk()

root.iconbitmap('tic tac toe.ico')
root.title('Tic Tac Toe by Wydiane')
root.resizable(False, False)

click = True
count = 0


board = [StringVar() for _ in range(9)]
def Rond(x1, y1):
    global C1, C2, C3
    Canvas.create_oval(x1-45, y1-45, x1+45, y1+45)
    
# ici on créer la fonction pour afficher les croix
def Croix(x1, y1):
    global C1, C2, C3
    Canvas.create_line(x1-45, y1-45, x1+45, y1+45)
    Canvas.create_line(x1+45, y1-45, x1-45, y1+45)


def play():
    global click, count
    while True:
        for i in range(3):
            for j in range(3):
                btn = Button(root, height=4, width=9, bd=.5, relief='ridge', bg='#d9b3ff',
                             textvariable=board[3*i+j], command=lambda row=i, col=j: press(row, col))

                btn.grid(row=i, column=j)
        if click:  # Player 1's turn
            croix = ('X')
            if count % 2 == 0:  # The first move is made by the AI
                ia(board, 'O')
                count += 1  # Update count after AI's move
                checkWin()
            click = not click
        else:  # Player 2's turn
            rond = ('O')
            Label(root, text=rond).grid(row=i, column=j)
            count += 1
            checkWin()
            if count == 9:  # All cells are occupied
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                root.quit()
                break
            click = not click
            
def ia(board, signe):
    # If it's the first move, play in a random cell
    if all(not cell.get() for cell in board):
        empty_cells = [i for i in range(9)]
        cell = random.choice(empty_cells)
    # Otherwise, play with the given signe to block the player's move
    else:
        for i in range(3):
            # Check rows
            if board[3*i].get() == board[3*i+1].get() == signe and not board[3*i+2].get():
                cell = 3*i+2
                break
            elif board[3*i].get() == board[3*i+2].get() == signe and not board[3*i+1].get():
                cell = 3*i+1
                break
            elif board[3*i+1].get() == board[3*i+2].get() == signe and not board[3*i].get():
                cell = 3*i
                break
            # Check columns
            elif board[i].get() == board[i+3].get() == signe and not board[i+6].get():
                cell = i+6
                break
            elif board[i].get() == board[i+6].get() == signe and not board[i+3].get():
                cell = i+3
                break
            elif board[i+3].get() == board[i+6].get() == signe and not board[i].get():
                cell = i
                break
        else:  # If no winning move is found, play in a random empty cell
            empty_cells = [i for i in range(9) if not board[i].get()]
            cell = random.choice(empty_cells)
    row = cell // 3
    col = cell % 3
    board[cell].set(signe)
    Label(root, text=signe).grid(row=row, column=col)


def press(row, col):
    global click, count
    btn = Button(root, height=4, width=9, bd=.5, relief='ridge', bg='#d9b3ff',
                 textvariable=board[3*row+col], command=lambda row=row, col=col: press(row, col))

    if click:  # Player 1's turn
        croix = ('X')
        board[3*row+col].set('X')
        Label(root, text=croix).grid(row=row, column=col)
        count += 1
        click = not click
        checkWin()
        if not click:  # If it's now Player 2's turn (i.e. click is False)
            # Call the AI function to play
            ia(board, 'O')
        else:  # Player 2's turn
                rond= ('O')
                board[3*row+col].set('O')
                Label(root, text=rond).grid(row=row, column=col)
                count += 1
                click = not click
                checkWin()

def checkWin():
    global count
    if (board[0].get() == board[1].get() == board[2].get() != '' or
        board[3].get() == board[4].get() == board[5].get() != '' or
        board[6].get() == board[7].get() == board[8].get() != '' or
        board[0].get() == board[3].get() == board[6].get() != '' or
        board[1].get() == board[4].get() == board[7].get() != '' or
        board[2].get() == board[5].get() == board[8].get() != '' or
        board[0].get() == board[4].get() == board[8].get() != '' or
        board[2].get() == board[4].get() == board[6].get() != ''):
        winner = "1" if not click else "2"
        messagebox.showinfo("Tic-Tac-Toe", "Player " + winner + " wins!")
        root.quit()
    elif count == 9:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        root.quit()



       
play()
root.mainloop()