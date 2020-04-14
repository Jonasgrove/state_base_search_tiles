#8 tile puzzle state based search solver
import copy


#solvegame
def solve8Tile(sState,goal):
    path = []
    return stateSearch([sState],goal,path)

def stateSearch(states,goal,path):
    if states == []:
        print(states)
        return states
    
    elif goal == states[0]:
        print(goal+path)
        return goal + path
    
    elif (states[0] in path) == True:      #cycle checker
        stateSearch(states[1:],goal,path)
        
    else:
        result = stateSearch(newMoves(states[0]),goal,states[0]+path)
        
        if result != []:
            return result            #trippy recursion
        else:
            stateSearch(states[1:],goal,path)

       
#generate new moves
def newMoves(board):
    allMoves = []
    for i in range(len(board)):
        for j in range(len(board)):
            if i == 0 or i == 1:            #if any tile in the first or second row is ontop of a one, swap them
                if board[i+1][j] == 0:      
                    allMoves.append(downSlide(i,j,board))
            if i == 1 or i == 2:             #if any tile in the 2nd or 3rd row is below a zero, swap them
                if board[i-1][j] == 0:
                    allMoves.append(upSlide(i,j,board))
            if j == 0 or j == 1:            #if any tile in the 1st or 2nd column is to the left of a zero, swap
                if board[i][j+1] == 0:
                    allMoves.append(rightSlide(i,j,board))
            if j == 1 or j == 2:            #if any tile in the 2nd or 3rd column is to the right of a zero, swap
                if board[i][j-1] == 0:
                    allMoves.append(leftSlide(i,j,board))
    return allMoves

#tile moving functions
def downSlide(i,j,board):
    newBoard = board
    temp = newBoard[i][j]
    newBoard[i][j] = newBoard[i+1][j]
    newBoard[i+1][j] = temp
    return newBoard

def upSlide(i,j,board):
    newBoard = board
    temp = newBoard[i][j]
    newBoard[i][j] = newBoard[i-1][j]
    newBoard[i-1][j] = temp
    return newBoard

def rightSlide(i,j,board):
    newBoard = board
    temp = newBoard[i][j]
    newBoard[i][j] = newBoard[i][j+1]
    newBoard[i][j+1] = temp
    return newBoard

def leftSlide(i,j,board):
    newBoard = board
    temp = newBoard[i][j]
    newBoard[i][j] = newBoard[i][j-1]
    newBoard[i][j-1] = temp
    return newBoard



solve8Tile([[1,0,3],[8,2,4],[7,6,5]],[[1,2,3],[8,0,4],[7,6,5]])
