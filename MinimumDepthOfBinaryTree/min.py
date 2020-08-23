import sys
sys.path.append("..")
from BasicTester import *

class Node:
   def __init__(self,val,left=None,right=None):
      self.val=val
      self.left=left
      self.right=right

def find(root):
   if(root==None):
      return 0

   minimum=1000000 # max number
   queue=[(root,1)]
   while(len(queue)!=0):
      node,count=queue.pop(0)
      found=0
      if(node.left!=None):
         queue.append((node.left,count+1))
         found+=1
      if(node.right!=None):
         queue.append((node.right,count+1))
      if(found==0 and minimum>count):
         minimum=count
   return minimum

node7=Node(7)
node15=Node(15)
node20=Node(20,node7,node15)
node9=Node(9)
node3=Node(3,node9,node20)

tester=BasicTester(find)
tester.test(node3,2)
