import sys
sys.path.append("..")
from BasicTester import *

def find(arr):
   sum1=sum(arr)
   sum2=0
   for i,x in enumerate(arr):
      if(2*sum2==sum1-x):
         return i
      sum2+=x
   return -1

tester=BasicTester(find)
tester.test([1,2,3,4,5,12,15],5)
tester.test([1,2,3,4],-1)
tester.test([1,2,3,67,1,5],3)
