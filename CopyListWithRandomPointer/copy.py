import sys
sys.path.append("..")
from BasicTester import *

class Node:
   def __init__(self,val,next=None,random=None):
      self.val=val
      self.next=next
      self.random=random

def copy(head:Node):
   tmp=head
   ret=None
   dict={None:None}  # old new values
   memory_node=None
   while(tmp!=None):
      if(ret==None):
         ret=Node(tmp.val)
         dict[tmp]=ret
         memory_node=ret  # save for return
      else:
         ret.next=Node(tmp.val)
         ret=ret.next
         dict[tmp]=ret
      tmp=tmp.next
   tmp=head
   ret=memory_node
   while(tmp!=None):
      ret.random=dict[tmp.random]
      tmp=tmp.next
      ret=ret.next

   return memory_node

def equal(a,b):
   while(a!=None):
      if(a.val!=b.val  or  ((a.random!=None and b.random!=None) and (a.random.val!=b.random.val ))  ):
         return False
      a=a.next
      b=b.next
   return True

node6=Node(34)
node5=Node(45,node6)
node4=Node(33,node5)
node3=Node(32,node4,node5)
node2=Node(3,node3,node5)
llnode1=Node(12,node2,node4)

llnode2=copy(llnode1)
print(equal(llnode1,llnode2))

