import sys
sys.path.append("..")
from BasicTester import *

def find(arr):
   ret=[]
   for x in arr:
      if(arr[abs(x)-1]<0):
         ret.append(abs(x))
      else:
         arr[abs(x)-1]*=-1
   return ret

tester=BasicTester(find)
tester.test([1,2,3,1,2],[1,2])
tester.test([2,2,1,3,4],[2])
tester.test([1,2,3,4,5],[])
