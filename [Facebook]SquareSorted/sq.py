import sys
sys.path.append("..")
from BasicTester import *

def sort(arr):
   tmp=[]
   for i in range(len(arr)):
      if(arr[0]>=0):
         break
      if(abs(arr[0])>abs(arr[len(arr)-i-1])):
         tmp=arr[0]
         del arr[0]
         arr.insert(len(arr)-i,tmp)
   return list(map(lambda x:x**2,arr))

testme=BasicTester(sort)
testme.test([-12,-3,0,1,2,3],[0,1,4,9,9,144])
testme.test([1,2,3,4],[1,4,9,16])
testme.test([-4,-3,-2,-1],[1,4,9,16])
