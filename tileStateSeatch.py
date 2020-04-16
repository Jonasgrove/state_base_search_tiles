#8 tile puzzle state based search solver
import copy


#solvegame
def solve8Tile(sState,goal):
    path = []
    recLimit = 50
    seen = []
    return stateSearch([sState],goal,path,recLimit,seen)

def stateSearch(states,goal,path,recLimit,seen):
    if states == []:
        print("exit1",states)
        return states
    
    elif goal == states[0]:
        print("exit success",goal+path)
        return goal + path

    else:
        if recLimit == 0:
          print([])
          print("states",states)
          print("path",path)
          return []
        else:
          moves,seen = newMoves(states[0],seen)
          result = stateSearch(moves,goal,[states[0]]+path,recLimit-1,seen)
        
          if result != []:
            return result            #trippy recursion
          else:
            stateSearch(states[1:],goal,path,recLimit-1,seen)

       
#generate new moves
def newMoves(board,seen):
    allMoves = []
    print("the board is",board)
    for i in range(len(board)):
        for j in range(len(board)):
            if i == 0 or i == 1:            #if any tile in the first or second row is ontop of a zero, swap them
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
    
    #check if move has already been tried
    counter = 0
    for i in allMoves:
      for j in seen:
        if i == j:
          del allMoves[counter]
          counter-=1
      counter+=1
    seen = allMoves + seen
    print("allMoves",allMoves)
    return allMoves, seen

#tile moving functions
def downSlide(i,j,board):
  board2 = copy.deepcopy(board)
  temp = board2[i][j]
  board2[i][j] = board2[i+1][j]
  board2[i+1][j] = temp
  print("down",board2)
  return board2

def upSlide(i,j,board):

  board2 = copy.deepcopy(board)
  temp = board2[i][j]
  board2[i][j] = board2[i-1][j]
  board2[i-1][j] = temp
  print("up",board2)
  return board2

def rightSlide(i,j,board):
  board2 = copy.deepcopy(board)
  temp = board2[i][j]
  board2[i][j] = board2[i][j+1]
  board2[i][j+1] = temp
  print("right",board2)
  return board2

def leftSlide(i,j,board):
  board2 = copy.deepcopy(board)
  temp = board2[i][j]
  board2[i][j] = board2[i][j-1]
  board2[i][j-1] = temp
  print("left",board2)
  return board2


#this start and goal state combination works
#solve8Tile([[1,2,3],[0,6,4],[8,7,5]],[[2,3,0],[1,6,4],[8,7,5]])
