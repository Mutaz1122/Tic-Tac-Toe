"""


Tic Tac Toe Player
"""

import math
import copy
from sympy import xfield
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
    numOfEmpty=0
    for x in board:
        for y in x:
            if(y==EMPTY):
                numOfEmpty=numOfEmpty+1

    if(numOfEmpty%2==0):
        return O
    else:
        return X                

        


    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos=set()
    
    for x in range(3):
        for y in range(3):
            if(board[x][y]==EMPTY):
                s=(x,y)
                pos.add(s)
    return pos            
  # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardnew=copy.deepcopy(board)
    #print(action)

    i,j=action
    
    if(boardnew[i][j]!=EMPTY ):
        raise Exception("errorrrrrrrrrrrrrrrrrrrrrrrrr")
    turn=player(boardnew)
    boardnew[i][j]=turn
    return boardnew



def winner(board):
    """
    Returns the winner of the game, if there is one.
    
    """
    
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2]==X):
            return X
        if(board[i][0]==board[i][1]==board[i][2]==O):
            return O
    for i in range(3):
        if(board[0][i]==board[1][i]==board[2][i]==X):
            return X
        if(board[0][i]==board[1][i]==board[2][i]==O):
            return O
    if(board[0][0]==board[1][1]==board[2][2]==X):
        return X
    if(board[0][0]==board[1][1]==board[2][2]==O):
        return O
    if(board[0][2]==board[1][1]==board[2][0]==X):
        return X
    if(board[0][2]==board[1][1]==board[2][0]==O):
        return O
    else:
        return None 
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    c=0
    for x in range(3):
        for y in range(3):
            if(board[x][y]!=EMPTY):
                c=c+1
                
    if(c==9):
        return True
    if(winner(board)==X or winner(board)==O):
        return True
    else:
        return False

    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """         
    if(terminal(board)==True):
        if(winner(board)==X):
            return 1
        elif (winner(board)==O):
            return -1
        else:
            return 0

def MaxValue(board):
    if terminal(board):
        return utility(board)
    v=-10
    for ac in actions(board):
        v=max(v,MinValue(result(board,ac)))
    return v    

def MinValue(board):
    if terminal(board):
        return utility(board)
    v=10
    for ac in actions(board):
        v=min(v,MaxValue(result(board,ac)))
    return v    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal==True):
        return None
    if(player(board)==X):
        t=tuple()
        v=-10
        for ac in actions(board):
            actionvalu=MinValue(result(board,ac))
            if(actionvalu==1):
                return ac
            elif(actionvalu>v):
                v=actionvalu
                t=ac
              
        return t
    
    elif (player(board)==O):
        t=tuple()
        v=10
        for ac in actions(board):
            actionvalu=MaxValue(result(board,ac))
            if(actionvalu==-1):
                return ac
            elif(actionvalu<v):
                v=actionvalu
                t=ac
                
        return t
    