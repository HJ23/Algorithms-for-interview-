def gol(board):
   for x in range(len(board)):
      for y in range(len(board[0])):
         counter=0
         for move in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
            new_x,new_y=x+move[0],y+move[1]
            if(new_x>=0 and new_x<len(board) and new_y>=0 and new_y<len(board[0])):
               counter+=board[new_x][new_y]==1 or board[new_x][new_y]==-1
         if(counter>3 and board[x][y]==1):
            board[x][y]=-1
         elif(counter<2 and board[x][y]==1):
            board[x][y]=-1
         elif(counter==3 and board[x][y]==0):
            board[x][y]=2
   for x in range(len(board)):
      for y in range(len(board[0])):
         if(board[x][y]==2):
            board[x][y]=1
         elif(board[x][y]==-1):
            board[x][y]=0

matrix=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

gol(matrix)
print(matrix)
