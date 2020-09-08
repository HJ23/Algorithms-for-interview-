import sys
sys.path.append("..")
from BasicTester import *

def find(arr):
   memory=set()
   sum=0
   for x in arr:
      sum+=x
      if(sum in memory):
         return True
      else:
         memory.add(sum)
   return False

tester=BasicTester(find)
tester.test([1,2,3,-3,4,5,6],True)
tester.test([-1,-2,-3,5,1],True)
tester.test([1,2,3,4,5,99],False)
