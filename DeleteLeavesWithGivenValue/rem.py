class Node:
   def __init__(self,val=0,right=None,left=None):
      self.val=val
      self.right=right
      self.left=left

def print_bt(root):
   ret=[]
   queue=[root]
   while(len(queue)!=0):
      node=queue.pop(0)
      ret.append(node.val)
      if(node.left):
         queue.append(node.left)
      if(node.right):
         queue.append(node.right)
   return ret


def rem(root,target):
   if(root):
      if(root.left!=None):
         root.left=rem(root.left,target)
      if(root.right!=None):
         root.right=rem(root.right,target)
      if(root.val==target and root.left==None and root.right==None):
         return None
   return root

node4=Node(2)
node5=Node(2)
node6=Node(4)
node3=Node(2,node4)
node2=Node(3,node6,node5)
node1=Node(1,node2,node3)

print(print_bt(node1))
rem(node1,2)
print(print_bt(node1))
