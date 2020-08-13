import sys
sys.path.append("..")
from BasicTester import *

def find(var):
   arr,k=var
   if(len(arr)%k!=0):
      return False

   dict={}
   for x in arr:
      if(x in dict):
         dict[x]+=1
      else:
         dict[x]=1
   counter=len(arr)
   while(counter!=0):
      minimum=min(dict.items(),key=lambda x:x[0])[0]
      for i in range(k):
         if(not minimum+i in dict):
            return False
         dict[minimum+i]-=1
         if(dict[minimum+i]==0):
            del dict[minimum+i]
      counter-=k
   return True


tester=BasicTester(find)
tester.test(([1,1,2,3,4,5],3),False)
tester.test(([3,2,1,2,3,4,3,4,5,9,10,11],3),True)
tester.test(([1,2,3,3,4,4,5,6],4),True)
tester.test(([3,3,2,2,1,1],3),True)
tester.test(([1,1,1,12,3,3,2,2],5),False)
