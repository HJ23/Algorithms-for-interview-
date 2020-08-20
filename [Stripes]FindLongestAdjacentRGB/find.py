def readFile(filename="test.txt"):
   matrix=[]
   text=""
   with open(filename,"r") as f:
      text=f.read()

   text=text.split("\n")[:-1]
   print(text)

   for x in text:
      tmp=[]
      x=x.split(" ")
      for let in x:
         tmp.append(let)
      matrix.append(tmp)
   return matrix

def createBin(row,col):
   ret=[]
   for _ in range(row):
      ret.append([0]*col)
   return ret


def solve(matrix):
#   print(matrix)
   row,column=len(matrix),len(matrix[0])
   binary=createBin(row,column)
   max=0
   for x in range(row):
      for y in range(column):
         if(matrix[x][y]=='E'):
            continue
         queue=[(x,y,matrix[x][y],1)]
         while(len(queue)!=0):
            x,y,typ,count=queue.pop(0)

            for move in [(1,0),(0,1),(-1,0),(0,-1)]:
               new_x=move[0]+x
               new_y=move[1]+y
               if(new_x<row and new_x>-1 and new_y<column and new_y>-1 and \
                  typ==matrix[new_x][new_y] ):

                  queue.insert(0,(new_x,new_y,typ,count+1))
                  if(count+1>max):
                     max=count+1
                  

   print(max)

solve(readFile())





