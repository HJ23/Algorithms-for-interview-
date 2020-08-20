import sys
sys.path.append("..")
from BasicTester import *

def find(matrix):
   if(matrix[0][0]==1):
      return -1
   binm=[]
   for _ in range(len(matrix)):
      binm.append([1]*len(matrix[0]))
   queue=[(0,0,1)]
   binm[0][0]=2
   shortest=10**8 # max int
   while(len(queue)!=0):
      x,y,count=queue.pop(0)
      if(x==len(matrix)-1 and y==len(matrix[0])-1 and shortest>count):
         shortest=count
      for move in [(0,1),(1,0),(1,1),(-1,1),(1,-1),(0,-1),(-1,0),(-1,-1)]:
         new_x,new_y=move[0]+x,move[1]+y
         if(new_x>=0 and new_x<len(matrix) and new_y>=0 and new_y<len(matrix[0]) \
             and binm[new_x][new_y]==1 and matrix[new_x][new_y]==0 ):
            queue.append((new_x,new_y,count+1))
            binm[new_x][new_y]=2

   return shortest if(shortest!=10**8) else -1

tester=BasicTester(find)
tester.test([[1,0,0],[1,1,0],[1,1,0]],-1)
tester.test([[0,0,0],[1,1,0],[1,1,0]],4)

