def symmetric(root):
   if(not root):
      return True
   q1=[root,root]

   while(len(q1)!=0):
      node1,node2=q1.pop(0),q1.pop(0)
      if(node1==None and node2==None):
         continue
      if((node1==None or node2==None) or node1.val!=node2.val):
         return False
      q1.append(node1.left)
      q1.append(node2.right)
      q2.append(node1.right)
      q2.append(node2.left)
   return True
