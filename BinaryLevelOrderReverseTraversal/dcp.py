import sys
sys.path.append("..")
from BasicTester import *


class Node:
   def __init__(self,val,left=None,right=None):
      self.val=val
      self.left=left
      self.right=right

def traverse(root):
   queue=[(root,0)]
   ret=[]
   pre=0
   tmp=[]
   while(len(queue)!=0):
      node,tf=queue.pop(0)
      if(pre!=tf):
         pre=tf
         ret+=tmp if(tf==1) else tmp[::-1]
         tmp=[]
      tmp.append(node.val)

      if(node.left!=None):
         queue.append((node.left,1 if(tf==0) else 0))
      if(node.right!=None):
         queue.append((node.right,1 if(tf==0) else 0 ))

   ret+=tmp if(pre==0) else tmp[::-1]
   return ret

node7=Node(7)
node6=Node(6)
node5=Node(5)
node4=Node(4)
node3=Node(3,node6,node7)
node2=Node(2,node4,node5)
test1=Node(1,node2,node3)

tester=BasicTester(traverse)
tester.test(test1,[1,3,2,4,5,6,7])
