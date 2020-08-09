def find(root):
   dic={}
   queue=[(root,0)] # node and level
   while(len(queue)!=0):
      node,level=queue.pop(0)
      if(level in dic):
         dic[level]=(node.val+dic[level][0],dic[level][1]+1)
      else:
         dic[level]=(node.val,1)  # value each level and count
      if(node.left!=None):
         queue.append((node.left,level+1))
      if(node.right!=None):
         queue.append((node.right,level+1))
   ret=[]
   for x in dic.items():
      level,values=x
      ret.append(values[0]/values[1])  # sum/count
   return ret


     
