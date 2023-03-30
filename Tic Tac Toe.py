from tkinter import *
from tkinter import messagebox

root = Tk()

root.iconbitmap('tic tac toe.ico')
root.title('Tic-Tac-Toe')
root.resizable(False, False)

click = True
count = 0

board = [StringVar() for _ in range(9)]
xPhoto = PhotoImage(file='X.png')
oPhoto = PhotoImage(file='O.png')

def play():
    for i in range(3):
        for j in range(3):
            btn = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#d9b3ff',
                         textvariable=board[3*i+j], command=lambda row=i, col=j: press(row, col))
            btn.grid(row=i, column=j)

def press(row, col):
    global click, count
    photo = xPhoto if click else oPhoto
    board[3*row+col].set('X' if click else 'O')
    Label(root, image=photo).grid(row=row, column=col)
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