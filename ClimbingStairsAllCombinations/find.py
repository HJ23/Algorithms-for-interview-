import sys

def solve(n):
   ret=[]
   queue=[([0],0)]
   while(len(queue)!=0):
      node,val=queue.pop(0)
      if(val==n):
         ret.append(tuple(node))
         continue

      for x in [1,2]:
         if( val+x <=n):
            tmp=node.copy()
            tmp.append(x)
            queue.append((tmp,val+x))
   return ret

print(solve(int(sys.argv[1])))

