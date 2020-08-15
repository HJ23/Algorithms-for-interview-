import sys
sys.path.append("..")
from BasicTester import *

def find(C):
   arr,target=C
   i=0
   j=len(arr)-1
   found=False
   while(i<=j):
      midd=(i+j)//2
      if(arr[midd]<target):
         i=midd+1
      elif(arr[midd]>target):
         j=midd-1
      else:
         found=True
         break
   if(not found):
      return [-1,-1]
   minimum=midd
   maximum=midd
   for x in range(1,midd+1):
      if(arr[midd-x]==target):
         minimum-=1
      else:
         break
   for x in range(midd+1,len(arr)):
      if(arr[x]==target):
         maximum+=1
      else:
         break
   return [minimum,maximum]


tester=BasicTester(find)
tester.test(([1,2,3,3,3,3,4,5,6,6,7],3),[2,5])
tester.test(([1,1,1,1,1,1,1,1,1,1],1),[0,9])
tester.test(([1,1,1,1,1,1],2),[-1,-1])
tester.test(([],23),[-1,-1])



