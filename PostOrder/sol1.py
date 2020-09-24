
def postorder1(root):
   ret=[]
   stack=[root]
   while(stack):
      node=stack.pop(0)
      ret.append(node.val)
      if(node.left):
         stack.insert(0,node.left)
      if(node.right):
         stack.insert(0,node.right)
   return ret[::-1]

def postorder2(root):
   if(root==None):
      return []
   return postorder2(root.left)+postorder2(root.right)+[root.val]
