# importing all necessary libraries
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy


def find_row_col(pos):
    row = int((pos-1)/3)  
    col = int(((pos-1)%3))
    return row, col


def checker(pos, txt):
    game = True
    row, col = find_row_col(pos)
    if(turn>3):
        if(gameboard[row][(col+1)%3]==txt):
            if(gameboard[row][(col+2)%3]==txt):
                game = False
        if(gameboard[(row+1)%3][col]==txt):
            if(gameboard[(row+2)%3][col]==txt):
                game = False
        if(pos in [1,5,9]):
            if(gameboard[(row+1)%3][(col+1)%3]==txt):
                if(gameboard[(row+2)%3][(col+2)%3]==txt):
                    game = False
        if(pos in [3,5,7]):
            if(gameboard[(row+1)%3][(col+2)%3]==txt):
                if(gameboard[(row+2)%3][(col+1)%3]==txt):
                    game = False
    return game

# Configure text on button while playing with another player
def get_text(pos, gb, l1, l2):
    global turn
    global gameboard
    txt = ""
    a, b = find_row_col(pos)
    if gameboard[a][b] == -1:
        if(turn%2 == 0):
            txt = "O"
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
        else:
            txt = "X"
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
        gameboard[a][b] = txt
        turn += 1
        button[pos-1].config(text=gameboard[a][b])
    if not checker(pos, txt):
        gb.destroy()
        box = messagebox.showinfo("{}\'s Wins".format(txt))
    elif(isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")

# Check the board is full or not

def isfull():
    global turn
    if turn == 9:
        return True
    else:
        False

def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    i = 1
    while i < 10:
        button.append(i)
        get_t = partial(get_text, i, game_board, l1, l2)
        button[i-1] = Button(game_board, bd=5, command=get_t, height=4, width=8)
        r, c = find_row_col(i)
        button[i-1].grid(row=3+r, column=c)
        i+=1
    game_board.mainloop()

def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player 1 : X", width=10, state=DISABLED)
    l1.grid(row=1, column=1)
    
    l2 = Button(game_board, text="Player 2 : O",
                width=10)
    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)

def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpl = partial(withplayer, menu)

    head = Button(menu, text="---Welcome to tic-tac-toe---",
                  activeforeground='red',
                  activebackground="yellow", bg="red",
                  fg="yellow", width=500, font='summer', bd=5)

    B1 = Button(menu, text="Play", command=wpl, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)

    B2 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    menu.mainloop()

# Global Variables
turn=0
gameboard = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

# Call main function
if __name__ == '__main__':
    play()

