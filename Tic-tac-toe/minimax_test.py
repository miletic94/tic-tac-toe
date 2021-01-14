import numpy as np

RESULT = False
def check_win():
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
    result = np.array([r, c, d1, d2, tbt])
    result = np.any(result)
    global RESULT 
    if result:
        print("WIN")
        RESULT = result

board = np.array([["X", "O", "", "O"],
                   ["", "O", "X", "X"],
                    ["", "X", "X", ""],
                    ["O", "0", "", "" ]])

pos_boards = []
index = np.where(board=="")
INDEX = [(index[0][i], index[1][i]) for i in range(len(index[1]))]

for i in INDEX:
    b = board.copy()
    b[i] = "X"
    pos_boards.append(b)

print(pos_boards)

# def minimax(board, depth, alpha, beta, is_maximizing):
#     if RESULT or depth == 0:
#         return score

#     if is_maximizing == True
#         maxEval = float("-inf")
        

