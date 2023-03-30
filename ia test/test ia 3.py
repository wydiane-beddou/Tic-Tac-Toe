from tkinter import *
from tkinter import messagebox
import random

root = Tk()

root.iconbitmap('tic tac toe.ico')
root.title('Tic Tac Toe by Wydiane')
root.resizable(False, False)


click = True
count = 0

board = [StringVar() for _ in range(9)]

def create_canvas():
    canvas = Canvas(root, width=90, height=90)
    canvas.pack()
    return canvas

def draw_croix(canvas, x1, y1):
    canvas.create_line(x1-45, y1-45, x1+45, y1+45)
    canvas.create_line(x1+45, y1-45, x1-45, y1+45)

canvas = Canvas(root, width=90, height=90)
canvas.pack()

draw_croix(canvas, 50, 50)

def play():
    global click, count
    canvas = create_canvas()
    if count % 2 == 0:  # The first move is made by the AI
        ia(board, 'O')
        count += 1  # Update count after AI's move
    while True:
        for i in range(3):
            for j in range(3):
                btn = Button(root, height=4, width=9, bd=.5, relief='ridge', bg='#d9b3ff',
                             textvariable=board[3*i+j], command=lambda row=i, col=j: press(row, col))
               
                btn.grid(row=i, column=j)
        if click:  # Player 1's turn
            signe = 'X'
        else:  # Player 2's turn
            signe = 'O'
            cell = ia(board, signe)
            row = cell // 3
            col = cell % 3
            board[cell].set(signe)
            if btn.cget("state") == "normal":
                Label(root, text=signe).grid(row=row, column=col)
            count += 1
        click = not click
        if checkWin():
            break
          
def checkWin():
        for i in range(3):
        # Check rows
            if board[3*i].get() == board[3*i+1].get() == board[3*i+2].get() and board[3*i].get():
                messagebox.showinfo("Tic Tac Toe", "Player " + board[3*i].get() + " wins!")
                restart()
        # Check columns
            elif board[i].get() == board[i+3].get() == board[i+6].get() and board[i].get():
                messagebox.showinfo("Tic Tac Toe", "Player " + board[i].get() + " wins!")
                restart()
        # Check diagonals
        if board[0].get() == board[4].get() == board[8].get() and board[0].get():
            messagebox.showinfo("Tic Tac Toe", "Player " + board[0].get() + " wins!")
            restart()
        elif board[2].get() == board[4].get() == board[6].get() and board[2].get():
            messagebox.showinfo("Tic Tac Toe", "Player " + board[2].get() + " wins!")
            restart()
        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            restart()
            


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
            elif board[i+3].get() == board[i+6].get() == signe and not board[i].get():
                cell = i
                break
            # Check columns
            elif board[i].get() == board[i+3].get() == signe and not board[i+6].get():
                cell = i+6
                break
            elif board[i].get() == board[i+6].get() == signe and not board[i+3].get():
                cell = i+3
                break
        else:
            # If there is no cell to block, play in an empty cell
            empty_cells = [i for i, cell in enumerate(board) if not cell.get()]
            cell = random.choice(empty_cells)
    
    return cell


def restart():
    global click, count
    for i in range(9):
        board[i].set('')
    click = True
    count = 0
    play()

def quit_game():
    root.destroy()

menu = Menu(root)
root.config(menu=menu)

game_menu = Menu(menu)
menu.add_cascade(label='Game', menu=game_menu)
game_menu.add_command(label='New game', command=restart)
game_menu.add_separator()
game_menu.add_command(label='Quit', command=quit_game)

play()
root.mainloop()