import numpy as np

pos_boards = []
board = np.array([["X","","O", "O"],
                  ["","X","", "O",],
                  ["","","X", ""],
                  ["","","",""]])
PLAYER = "X"
def check_win(board):
    # VARIABLES:
    # win  holding did someno win (true/false)
    # score holding score based on who won
    # wining_strike # holding what is strike that led to win
    score = 0
    # rows
    r = np.any(np.all(board == PLAYER, axis = 1))
    # columns
    c = np.any(np.all(board == PLAYER, axis = 0))
    # diagonals
    d1_index = [range(0,4), range(0,4)]
    d1 = board[tuple(d1_index)]
    d1 = np.any(np.all(d1 == PLAYER))

    d2_index = [range(0,4),range(3,-1,-1)]
    d2 = board[tuple(d2_index)]
    d2 = np.any(np.all(d2 == PLAYER))
    
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
            # ADD WINING STRIKE FOR BOXES
    # two by two [OPTIMIZE] 

    # result
    win = np.array([r, c, d1, d2])
    win = np.any(win)
    if win == True:
        if PLAYER == "X":
            score = 1
        elif PLAYER == "O":
            score = -1

            # If result isn't True you don't have to do this
    # returning wining strike
    wining_strike = None 
#    if r:
#        wining_strike = np.array([[button_index[0]]*4, range(0,4)])
#    elif c: wining_strike = np.array([range(0,4), [button_index[0]]*4])
#    elif d1:
#        wining_strike = d1_index
#    elif d2:
#        wining_strike = d2_index
    return {
        "win":win,
        "score":score,
        "wining_strike":wining_strike
    }

"""
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
"""  

def minimax(board, depth, alpha, beta, is_maximizing):
    
    empty = np.where(board=="")
    empty = [(empty[0][i], empty[1][i]) for i in range(len(empty[1]))]
    score = check_win(board)
    if depth == 0 or len(empty) < 1 or score["win"] == True:
        return score["score"]
    
    if is_maximizing == True:
        maxEval = float("-inf")
        for e in empty:
            b = board.copy()
            b[e] = "X"
            ev = minimax(b, depth-1, float("-inf"), float("inf"), False)

            pos_boards.append(b)
            
            maxEval = max(maxEval, ev)
            alpha = max(alpha, ev)
            if beta <= alpha:
                return
        return maxEval
 
    if is_maximizing == False:
        minEval = float("inf")
        for e in empty:
            b = board.copy()
            b[e] = "O"
            ev = minimax(b, depth-1, float("-inf"), float("inf"), True)
            
            pos_boards.append(b)
            
            minEval = min(minEval, ev)
            beta = min(beta, ev)
            if beta <= alpha:
                return
        return minEval

print(minimax(board, 1, float("-inf"), float("inf"), True))
print(len(pos_boards))