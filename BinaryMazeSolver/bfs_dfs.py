import math

maze=[
      [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0],
      [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
      [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
      [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0],
      [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
      [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0],
      [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
      [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0],
      [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
      [0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0],
      [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
      [0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0],
      [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
      [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1]
]


bmap=[]

def refresh_map():
    global bmap
    bmap=[]
    for _ in range(len(maze)):
        tmp=[]
        for _ in range(len(maze[0])):
            tmp.append(0)
        bmap.append(tmp)

#assert(  (len(bmap)==len(maze)) and (len(bmap[0])==len(maze[0]))   )



class node(object):
    def __init__(self,row,column,counter=1,pre=None):
        self.r=row
        self.c=column
        self.counter=counter
        self.pre=pre


def check(row,column):
    return row<len(maze) and column<len(maze[0]) and row>=0 and column>=0 and maze[row][column]==1 and bmap[row][column]==0

def solve_BFS(start=(0,0),end=(len(maze)-1,len(maze[0])-1)):
    queue=[node(start[0],start[1])]
    moves=[(0,1),(1,0),(0,-1),(-1,0)]

    while(len(queue)!=0):
        node_=queue[0]
        del queue[0]

        for move in moves:
            if(check(node_.r+move[0],node_.c+move[1])):
                if(node_.r+move[0]==end[0] and node_.c+move[1]==end[1]):
                    print("path found {}".format(node_.counter+1))
                    pre=node_
                    print((node_.r+move[0],node_.c+move[1]))
                    while(pre!=None):
                        print((pre.r,pre.c))
                        pre=pre.pre
                    return
                else:
                    queue.append(node(node_.r+move[0],node_.c+move[1],counter=node_.counter+1,pre=node_))
        bmap[node_.r][node_.c]=1


def solve_DFS(start=(0,0),end=(len(maze)-1,len(maze[0])-1)):
    queue=[node(start[0],start[1])]
    moves=[(0,1),(1,0),(0,-1),(-1,0)]

    while(len(queue)!=0):
        node_=queue[0]
        del queue[0]

        for move in moves:
            if(check(node_.r+move[0],node_.c+move[1])):
                if(node_.r+move[0]==end[0] and node_.c+move[1]==end[1]):
                    print("path found {}".format(node_.counter+1))
                    pre=node_
                    print((node_.r+move[0],node_.c+move[1]))
                    while(pre!=None):
                        print((pre.r,pre.c))
                        pre=pre.pre
                    return
                else:
                    queue.insert(0,node(node_.r+move[0],node_.c+move[1],counter=node_.counter+1,pre=node_))
        bmap[node_.r][node_.c]=1

import time

refresh_map()
start=time.time()
solve_BFS()
print("***************************************************")
print("elapsed time BFS: {} sec".format(time.time()-start))
print("***************************************************")
refresh_map()
start=time.time()
solve_DFS()
print("elapsed time DFS: {} sec".format(time.time()-start))


