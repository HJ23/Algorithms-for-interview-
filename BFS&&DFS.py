# Complexity for BFS O(n)
# Complexity for DFS O(n)
import os

class node():
    element=None
    left=None
    right=None
    def __init__(self,element=None):
        self.element=element
    def __repr__(self):
        return str(self.element)

class BinaryTree():
    head=None
    current=None
    nodes=[]
    def add(self,element):
        temp=node(element)
        if(self.head==None):
            self.head=temp
            self.current=self.head
            self.nodes.append(self.head)
        else:
            if(self.nodes[0].left==None and self.nodes[0].element>temp.element):
                self.nodes[0].left=temp
                self.nodes.append(temp)
            elif(self.nodes[0].right==None):
                self.nodes[0].right=temp
                self.nodes.append(temp)
            if(self.nodes[0].left!=None and self.nodes[0].right!=None):
                self.nodes.pop(0)
                
    def printTreeBFS(self):
        queue=[self.head]
        while(len(queue)!=0):
            temp=queue.pop(0)
            if(temp!=None):
                queue.append(temp.left)
                queue.append(temp.right)
                print(temp.element)
    def printTreeDFS(self):
        stack=[self.head]
        while(len(stack)!=0):
            temp=stack.pop(0)
            if(temp!=None):
                stack.insert(0,temp.right)
                stack.insert(0,temp.left)
                print(temp.element)
                    
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

            
            
            
            
            
            
            
            


