import sys
sys.path.append("..")
from BasicTester import *

class TreeNode:
   def __init__(self,val,left=None,right=None):
      self.val=val
      self.left=left
      self.right=right


def check_multi(v):
   a,b=v
   if(len(a)!=len(b)):
      return False
   for x  in range(len(a)):
      if(len(a[x])!=len(b[x])):
         return False
      for y in range(len(a[0])):
         if(a[x][y]!=b[x][y]):
            return False
   return True



def get(root:TreeNode):
   if(root==None):
      return []
   ret=[[root.val]]
   queue=[(root,1)]
   while(len(queue)!=0):
      node,level=queue.pop(0)
      if(node.left!=None):
         if(len(ret)<level+1):
            ret.append([node.left.val])
         else:
            ret[level].append(node.left.val)
         queue.append((node.left,level+1))
      if(node.right!=None):
         if(len(ret)<level+1):
            ret.append([node.right.val])
         else:
            ret[level].append(node.right.val)
         queue.append((node.right,level+1))
   return ret[::-1]


tester=BasicTester(check_multi)

tmp1=TreeNode(12,None,TreeNode(34,None,None))
tmp2=TreeNode(56,None,TreeNode(562,None,TreeNode(67,TreeNode(5,None,None),None)))
test1=TreeNode(45,tmp1,tmp2)

tester.test((get(test1),[[5],[67],[34,562],[12,56],[45]]),True)
tester.test((get(test1),[[5],[67],[34,562],[12,56,1],[45]]),False)
