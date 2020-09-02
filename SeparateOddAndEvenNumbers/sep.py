import sys
sys.path.append("..")
from BasicTester import *


def separate(arr):
   if(len(arr)<=2):
      return arr if(arr[0]%2==0) else arr[::-1]

   i=0
   j=1
   while(j!=len(arr) and i!=len(arr)):   # left even right odd
      if(arr[i]%2==1 and arr[j]%2==0 ):
         tmp=arr[i]
         arr[i]=arr[j]
         arr[j]=tmp
         i+=1
         j+=1
      elif(arr[i]%2==0 and arr[j]%2==0):
         i+=1
         j+=1
      elif(arr[i]%2==1 and arr[j]%2==1):
         j+=1
      elif(arr[i]%2==0 and arr[j]%2==1):
         i+=1
         j+=1
   return arr

tester=BasicTester(separate)
tester.test([1,2,3,4,5],[2,4,3,1,5])
tester.test([2,4,6,8],[2,4,6,8])
tester.test([1,3,4,5,7,8,10],[4,8,10,5,7,3,1])
tester.test([1,2],[2,1])

