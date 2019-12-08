# Complexity for BFS O(n)
# Complexity for DFS O(n)

class Node():
    def __init__(self,__value__=None):
        self.left=None
        self.right=None
        self.value=__value__
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def setRight(self,node):
        self.right=node
    def setLeft(self,node):
        self.left=node

class BinaryTree():
    def __init__(self):
        self.queue=[]
        self.root=None
    def add(self,value):
        tempnode=Node(value)
        if(self.root==None):
            self.root=tempnode
            self.queue.append(self.root)
        else:
            current=self.root
            previous=self.root
            while(True):
                if(current.value<=tempnode.value):
                    previous=current
                    current=current.getRight()
                    if(current==None):
                        previous.setRight(tempnode)
                        break
                elif(current.value>tempnode.value):
                    previous=current
                    current=current.getLeft()
                    if(current==None):
                        previous.setLeft(tempnode)
                        break   
                
    def printTreeBFS(self):
        queue=[self.root]
        while(len(queue)!=0):
            temp=queue.pop(0)
            if(temp!=None):
                queue.append(temp.left)
                queue.append(temp.right)
                print(temp.value)
    def printTreeDFS(self):
        stack=[self.root]
        while(len(stack)!=0):
            temp=stack.pop(0)
            if(temp!=None):
                stack.insert(0,temp.right)
                stack.insert(0,temp.left)
                print(temp.value)
                    
#          34
#    27         67
#13    89    32   NULL
                
temp=BinaryTree()  
temp.add(34)
temp.add(27)
temp.add(67)
temp.add(13)
temp.add(89)
temp.add(32)
temp.add(None)
print("Deep First Search")
temp.printTreeDFS()
print("Breatdh First Search")
temp.printTreeBFS()
