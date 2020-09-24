
def preorder(root):
   if(root==None):
      return
   return [root.val]+preorder(root.left)+preorder(root.right)

def preorder(root):
   ret=[]
   stack=[root]
   while(stack):
      node=stack.pop()
      ret.append(node.val)
      if(node.right):
         stack.append(node.right)
      if(node.left):
         stack.append(node.left)
   return ret

