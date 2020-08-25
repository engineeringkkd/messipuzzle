import copy
#class Board used to represent our puzzle
class Board:
  def __init__(self,board):
    self.board=board
    self.father=None
  def __eq__(self,other):
    return self.board==other.board
  def __repr__(self):
    return f"Board({self.board})"
  def __str__(self):
    return  str(self.board[0]) + "\n" + str(self.board[1]) + "\n"+ str(self.board[2])
  def __hash__(self):
        return hash((self.board))
  
  def up(self):
    #function to return what will be the state if we move the blank cell(0) up
    for i in self.board:
      if 0 in i:
        index=(self.board.index(i),i.index(0))
    current_board_state=copy.deepcopy(self.board)
    if index[0]==0:
      return False
    else:
      upindex=(index[0]-1,index[1])
      upelement=current_board_state[upindex[0]][upindex[1]]
      current_board_state[upindex[0]][upindex[1]]=0
      current_board_state[index[0]][index[1]]=upelement
    return current_board_state
  def down(self):
    #function to return what will be the state if we move the blank cell(0) down
    for i in self.board:
      if 0 in i:
        index=(self.board.index(i),i.index(0))
    current_board_state=copy.deepcopy(self.board)
    if index[0]==2:
      return False
    else:
      downindex=(index[0]+1,index[1])
      downelement=current_board_state[downindex[0]][downindex[1]]
      current_board_state[downindex[0]][downindex[1]]=0
      current_board_state[index[0]][index[1]]=downelement
    return current_board_state
  
  def right(self):
    #function to return what will be the state if we move the blank cell(0) right
    for i in self.board:
      if 0 in i:
        index=(self.board.index(i),i.index(0))
    current_board_state=copy.deepcopy(self.board)
    if index[1]==2:
      return False
    else:
      rightindex=(index[0],index[1]+1)
      rightelement=current_board_state[rightindex[0]][rightindex[1]]
      current_board_state[rightindex[0]][rightindex[1]]=0
      current_board_state[index[0]][index[1]]=rightelement
    return current_board_state
  def left(self):
    #function to return what will be the state if we move the blank cell(0) left
    for i in self.board:
      if 0 in i:
        index=(self.board.index(i),i.index(0))
    current_board_state=copy.deepcopy(self.board)
    if index[1]==0:
      return False
    else:
      leftindex=(index[0],index[1]-1)
      leftelement=current_board_state[leftindex[0]][leftindex[1]]
      current_board_state[leftindex[0]][leftindex[1]]=0
      current_board_state[index[0]][index[1]]=leftelement
    return current_board_state

def generate_level(board):
  #this function extend the current state of board to next possible states
  templist=[board.up(),board.down(),board.left(),board.right()]
  numberof_falses=templist.count(False)
  for i in range(numberof_falses):
    templist.remove(False)
  retlist=[]
  for things in templist:
    retlist.append(Board(things))
  return retlist
##
##                   
##
##def search(start):
##  #this function searches(BFS) for our goal
##  q=[]
##  q.append([start])
##  while True:
##    if Board([[1,2,3],[4,5,6],[7,8,0]]) in q[0]:
##      return q[0]
##    add=generate_level(q[0][-1])
##    for thing in add:
##      if thing not in q[0]:
##        q.append(q[0]+[thing])
##    q.remove(q[0])
##def seethesol(sol):
##  for i in range(len(sol)-1):
##    before=sol[i]
##    after=sol[i+1]
##    if before.up()==after.board:
##      print("move the blank cell up")
##    elif before.down()==after.board:
##      print("move the blank cell down")
##    elif before.right()==after.board:
##      print("move the blank cell right")
##    else:
##      print("move the blank cell left")
##x=input("enter the Board")
##temp= x.split(" ")
##actuallist=[]
##for i in temp:
##  actuallist.append(int(i))
###print(actuallist)
##brd=Board([actuallist[0:3],actuallist[3:6],actuallist[6:9]])
###print(brd)
##seethesol(search(brd))
##  


    
  
    
  
    
    
    
  
  
  
                          
       
  
