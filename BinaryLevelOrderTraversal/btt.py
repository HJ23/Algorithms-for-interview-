class Node:
   def __init__(self,val,left=None,right=None):
      self.val=val
      self.left=left
      self.right=right

def traverse(root):
   pre=0
   ret=[]
   tmp=[]
   queue=[(root,0)]
   while(len(queue)!=0):
      node,tf=queue.pop(0)
      if(pre!=tf):
         ret.append(tmp)
         tmp=[]
         pre=tf
      tmp.append(node.val)
      if(node.left!=None):
         queue.append((node.left,1 if(tf==0) else 0))
      if(node.right!=None):
         queue.append((node.right,1 if(tf==0) else 0))
   ret.append(tmp)
   return ret

node7=Node(7)
node6=Node(6)
node5=Node(5)
node4=Node(4)
node3=Node(3,node6,node7)
node2=Node(2,node4,node5)
test=Node(1,node2,node3)

print(traverse(test))
