import copy

MapOfMaze=[[1,1,1,1,1,1,1,1,1],
          [1,0,1,0,0,1,0,0,1],
          [1,0,1,0,0,1,0,1,0],
          [1,0,0,1,1,1,1,1,1],
          [1,1,1,1,0,1,0,0,0],
          [1,1,1,1,1,1,1,1,1],
          [1,0,1,1,0,0,0,0,1],
          [1,0,1,1,1,1,0,0,1],
          [1,1,1,0,1,0,1,1,1],
          [1,1,1,0,1,1,1,1,1]
]

class PathFinder():
    def __init__(self,map):
        self.result=copy.deepcopy(map)
        self.array=copy.deepcopy(map)
        self.map=[]
        self.__arraySIZE=[len(map),len(map[0])]
        for x in range(len(self.array)):
            tmp=[]
            for y in range(len(self.array[0])):
                tmp.append(False)
            self.map.append(tmp)

    class Node():
        def __init__(self,coord,dist):
            self.coordinatesROW=coord[0]
            self.coordinatesCOLUMN=coord[1]
            self.distance=dist
            self.previous=None
        def setPrevious(self,node):
            self.previous=node
            
    def checkValidity(self,coordinates):
        ROW=coordinates[0]
        COLUMN=coordinates[1]
        if((ROW>=0 and ROW<self.__arraySIZE[0]) and (COLUMN>=0 and COLUMN<self.__arraySIZE[1])):
            if(not self.map[ROW][COLUMN] and self.array[ROW][COLUMN]==1):
                return True
        return False
    
    def printMAP(self,MAP):
        tmp=""
        for row in range(self.__arraySIZE[0]):
            for column in range(self.__arraySIZE[1]):
                tmp+=str(MAP[row][column])+"  "
            tmp+="\n"
            
        print(tmp)

    def findBFS(self,start,stop):
        queue=[self.Node(start,0)]
        moves=[[0,1],[0,-1],[1,0],[-1,0]]
        found=False
        lastNode=None
        while(len(queue)!=0 and not found):
            node=queue[0]
            queue.pop(0)
            for move in moves:
                if(self.checkValidity([node.coordinatesROW+move[0],node.coordinatesCOLUMN+move[1]])):
                    self.array[node.coordinatesROW][node.coordinatesCOLUMN]=node.distance
                    queue.append(self.Node([node.coordinatesROW+move[0],node.coordinatesCOLUMN+move[1]],node.distance+1))
                    queue[-1].setPrevious(node)
                    if([node.coordinatesROW+move[0],node.coordinatesCOLUMN+move[1]]==stop):
                        self.array[node.coordinatesROW+move[0]][node.coordinatesCOLUMN+move[1]]=node.distance+1
                        print("Path Found!\n")
                        found=True
                        lastNode=queue[-1]
        
        while(lastNode!=None):
            row=lastNode.coordinatesROW
            column=lastNode.coordinatesCOLUMN
            self.result[row][column]="-"
            lastNode=lastNode.previous
        
        self.printMAP(self.result)
        
pf=PathFinder(MapOfMaze)
pf.findBFS([0,0],[9,8])


