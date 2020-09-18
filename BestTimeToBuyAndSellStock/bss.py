import sys
sys.path.append("..")
from UniTester import *

def bss(arr):
   maxi=0
   start=1000000000
   for x in arr:
      if(x<start):
         start=x
      else:
         maxi=max(maxi,(x-start))
   return maxi

@timer
@unitest(target=4)
def test1(arr=[1,2,3,4,5]):
   return bss(arr)

@timer
@unitest(target=10)
def test2(arr=[2,3,7,12,8,3]):
   return bss(arr)


@timer
@unitest(target=0)
def test3(arr=[9,8,7,6,5,4,3,2,1]):
   return bss(arr)



assert test1()
assert test2()
assert test3()

