
class Node:
   def __init__(self,val,left=None,right=None):
      self.val=val
      self.right=right
      self.left=left



def find(root):
   leftmost=root.val
   queue=[root]
   while(len(queue)!=0):
      node=queue.pop(0)
      leftmost=node.val
      if(node.right!=None):
         queue.append(node.right)
      if(node.left!=None):
         queue.append(node.left)
   return leftmost

node7=Node(7)
node4=Node(4)
node5=Node(5,left=node7)
node6=Node(6)
node2=Node(2,left=node4)
node3=Node(3,node5,node6)
node1=Node(1,node2,node3)

# expected leftmost : 7 
print(find(node1))
