import sys
sys.path.append("..")
from BasicTester import *


def find(arr):
   A=set(arr)
   longest=0
   for i,x in enumerate(arr):
      for y in arr[i+1:]:
         if(x+y in A):
            counter=2
            t=x
            while(True):
               if(t+y in A):
                  counter+=1
                  t,y=y,t+y
               else:
                  break
            if(counter>longest):
               longest=counter
   return longest


tester=BasicTester(find)
tester.test([1,2,3,4,5,7,8,9,10,12],5)
tester.test([3,4,5,6,7,9,12,21],4)

