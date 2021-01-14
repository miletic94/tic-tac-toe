import numpy as np
import tkinter as tk
import tkinter.messagebox
import random

board = np.empty((4,4), dtype=str)
players = ["X", "O"] 

# Randomly choose first player to go
player_index = random.randint(0,1)
PLAYER = players[player_index]

# Result
RESULT = False

def update_player(index):
    global PLAYER 
    global player_index

    if index == 0:
        index = index + 1
    elif index == 1:
        index = index - 1

    PLAYER = players[index]
    player_index = index

# [OPTIMIZE]
def check_win(board):
    win # holding did someno win (true/false)
    score = None # holding score based on who won
    wining_strike # holding what is strike that led to win

    # rows
    r = np.any(np.all(board == PLAYER, axis = 1))
    # columns
    c = np.any(np.all(board == PLAYER, axis = 0))
    # diagonals
    d1_index = [range(0,4), range(0,4)]
    d1 = board[d1_index]
    d1 = np.any(np.all(d1 == PLAYER))

    d2_index = [range(0,4),range(3,-1,-1)]
    d2 = board[d2_index]
    d2 = np.any(np.all(d2 == PLAYER))
            
            # ADD WINING STRIKE FOR BOXES
    # two by two [OPTIMIZE]
    two_by_two = np.array([board[0:2, 0:2],
                            board[0:2, 1:3],
                            board[0:2, 2:4],
                            board[1:3, 0:2],
                            board[1:3, 1:3],
                            board[1:3, 2:4],
                            board[2:4, 0:2],
                            board[2:4, 1:3],
                            board[2:4, 2:4]])
    tbt = np.array([np.all(i==PLAYER) for i in two_by_two])
    tbt = np.any(tbt)

    # result
    win = np.array([r, c, d1, d2, tbt])
    win = np.any(result)
    if win == True:
        if PLAYER == "X":
            score = 1
        elif PLAYER == "O":
            score = -1

            # If result isn't True you don't have to do this
    # returning wining strike
    wining_strike = None 
    if r:
        wining_strike = np.array([[button_index[0]]*4, range(0,4)])
    elif c: wining_strike = np.array([range(0,4), [button_index[0]]*4])
    elif d1:
        wining_strike = d1_index
    elif d2:
        wining_strike = d2_index
    
    return {
        "win":win,
        "score":score,
        "wining_strike":wining_strike
    }

def result():
    return str(PLAYER + " won!")

def check_tie():
    if np.all(board!=""):
        print("TIE")
        tkinter.messagebox.showinfo(title="GAME OVER", message="The game is tied")  
        reset()

def render_view():
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16]
    for b in buttons:
        b.config(text=board[b.grid_info()["row"], b.grid_info()["column"]])
    
    # COLOR WINING STRIKE

def print_status():
    if RESULT == True:
        tkinter.messagebox.showinfo(title="GAME OVER", message=result())
        reset()
        

def reset():
    global board
    board = np.empty((4,4), dtype=str)   

    global RESULT
    RESULT = False

    # Randomly choose first player to go
    global player_index
    player_index = random.randint(0,1)

    global PLAYER
    PLAYER = players[player_index]

    render_view()
    print("Reset called")

root = tk.Tk()
root.title("tic-tac-toe")
#Kada kliknem na button da vrati grid_info, i te podatke upisujemo u varijablu board

b1 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b1))
b2 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b2))
b3 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b3))
b4 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b4))

b5 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b5))
b6 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b6))
b7 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b7))
b8 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b8))

b9 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b9))
b10 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b10))
b11 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b11))
b12 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b12))

b13 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b13))
b14 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b14))
b15 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b15))
b16 = tk.Button(root, text = " ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: update_board(b16))


b1.grid(row="0", column="0")
b2.grid(row="0", column="1")
b3.grid(row="0", column="2")
b4.grid(row="0", column="3")

b5.grid(row="1", column="0")
b6.grid(row="1", column="1")
b7.grid(row="1", column="2")
b8.grid(row="1", column="3")

b9.grid(row="2", column="0")
b10.grid(row="2", column="1")
b11.grid(row="2", column="2")
b12.grid(row="2", column="3")

b13.grid(row="3", column="0")
b14.grid(row="3", column="1")
b15.grid(row="3", column="2")
b16.grid(row="3", column="3")

# Updates board array with tic of a player whos turn it is
def update_board(b):
    global button_index
    button_index = tuple([b.grid_info()["row"], b.grid_info()["column"]])
    if board[button_index] == "":
        board[button_index] = PLAYER
        print(board)
        check_win()
        result()
        check_tie()
        render_view()
        print_status()
        update_player(player_index)
        
    else:
        pass


root.mainloop()
