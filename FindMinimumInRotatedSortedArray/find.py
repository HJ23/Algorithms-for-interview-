import sys
sys.path.append("..")
from BasicTester import *

def find(arr):
   i=0
   j=len(arr)-1
   while(i<=j):
      if(abs(i-j)<=1):
         return min(arr[i],arr[j])
      midd=(j+i)//2
      if(arr[midd]>arr[i] and arr[midd]>arr[j]):
         i=midd
      elif(arr[midd]>arr[i] and arr[midd]<arr[j]):
         j=midd
      elif(arr[midd]<arr[j] and arr[midd]<arr[i] ):
         j=midd

tester=BasicTester(find)
tester.test([1,2,3,4,5],1)
tester.test([3,4,5,6,1,2],1)
tester.test([5,1,2,3,4],1)
tester.test([2,3,4,5,1],1)
