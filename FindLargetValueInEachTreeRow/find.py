import sys
sys.path.append("..")
from BasicTester import *

class Node:
   def __init__(self,val,left=None,right=None):
      self.right=right
      self.left=left
      self.val=val

def find(node):
   diction={}
   queue=[(node,0)]
   while(len(queue)!=0):
      node,level=queue.pop(0)
      if(level in diction):
         if(diction[level]<node.val):
            diction[level]=node.val
      else:
         diction[level]=node.val

      if(node.left!=None):
         queue.append((node.left,level+1))
      if(node.right!=None):
         queue.append((node.right,level+1))

   diction=sorted(diction.items(),key=lambda x:x[0])
   return list(map(lambda x:x[1],diction))


node1=Node(12,Node(34,Node(45)),Node(33,Node(56,Node(123))))
node2=Node(0,Node(33),Node(45,Node(111,Node(12))))

tester=BasicTester(find)
tester.test(node1,[12,34,56,123])
tester.test(node2,[0,45,111,12])
