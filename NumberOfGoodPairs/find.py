import sys
sys.path.append("..")
from BasicTester import *


def find(arr):
   dict={}
   for x in arr:
      if(x in dict):
         dict[x]+=1
      else:
         dict[x]=1
   counter=0
   for x in list(dict.values()):
      x-=1
      counter+=x*(x+1)//2
   return counter


tester=BasicTester(find)
tester.test([1,2,3,4],0)
tester.test([1,2,1,2,3,1,1,1],11)
