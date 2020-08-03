import copy

let=[["A","B","C","E"],
     ["S","F","E","S"],
     ["A","D","E","E"]]


            

def check(r,c,limitr,limitc,tfmaze):
   return (r<limitr) and (c<limitc) and (r>=0) and (c>=0) and tfmaze[r][c]==0


def tf(limit_r,limit_h):
   tf_maze=[]

   for _ in range(limit_r):
      tmp=[]
      for _ in range(limit_h):
         tmp.append(0)
      tf_maze.append(tmp)
   
   return tf_maze

def find(maze,word="ABCESEEEFS"):

   limit_r=len(maze)
   limit_h=len(maze[0])
   
   for x in range(limit_r):
      for y in range(limit_h):
         if(maze[x][y]==word[0]):

            tf_maze=tf(limit_r,limit_h)
            tf_maze[x][y]=1
            stack=[((x,y),1,tf_maze)]
            while(len(stack)!=0):
               node,count,tf_maze=stack.pop(0)
               tf_maze[node[0]][node[1]]=count
               
               if(count==len(word)):
                  return True
               
               for move in  [ (1,0),(0,1),(0,-1),(-1,0) ]:
                  add_x=node[0]+move[0]
                  add_y=node[1]+move[1]
                  if(check(add_x,add_y,limit_r,limit_h,tf_maze) and word[count]==maze[add_x][add_y]):
                     stack.insert(0,(( add_x,add_y ),count+1,copy.deepcopy(tf_maze)))
                     
                     
                     
   return False


print(find(let))











