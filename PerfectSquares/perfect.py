import sys
sys.path.append("..")
from BasicTester import *

def find(n):
   squares=[x*x for x in range(int(n**0.5),0,-1)]
   queue=[(n,0,0)]  # number count index
   while(len(queue)!=0):
      val,count,index=queue.pop(0)
      for k,v in enumerate(squares[index:]):
         tmp=val-v
         if(tmp<0):
            continue
         if(tmp==0):
            return count+1
         queue.append((tmp,count+1,k))

tester=BasicTester(find)
tester.test(12,3)
tester.test(13,2)
tester.test(7168,4)




