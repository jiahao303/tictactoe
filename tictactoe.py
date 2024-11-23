"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if sum(sublist.count(X) for sublist in board) == sum(sublist.count(O) for sublist in board):
        return X
    else:
        return O 
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()
    for i, sublist in enumerate(board):
        for j, value in enumerate(sublist):
            if value is EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action
    deepcopy = copy.deepcopy(board)
    if not (0 <= i <= 2) or not (0 <= j <= 2) or deepcopy[i][j] is not EMPTY:
        raise Exception
    else:
        deepcopy[i][j] = player(board)
        return deepcopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]
        
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] is not EMPTY:
        return board[1][1]
    
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] is not EMPTY:
        return board[1][1]

    return None    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
        
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maxvalue(board):
        v = -math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = max(v, minvalue(result(board, action)))
        return v

    def minvalue(board):
        v = math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, maxvalue(result(board, action)))
        return v

    if terminal(board):
        return None
    
    if player(board) is X:
        v = -math.inf
        for action in actions(board):
            if minvalue(result(board, action)) > v:
                v = minvalue(result(board, action))
                a = action
        return a
    
    elif player(board) is O:
        v = math.inf
        for action in actions(board):
            if maxvalue(result(board, action)) < v:
                v = maxvalue(result(board, action))
                a = action
        return a