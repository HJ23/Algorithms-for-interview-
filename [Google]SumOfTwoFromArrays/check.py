import sys
sys.path.append("..")
from BasicTester import *

def check(A):
   arr1,arr2,val=A
   arr2=set(arr2)
   for a in arr1:
      if( (val-a) in arr2 ):
         return True
   return False

testme=BasicTester(check)
testme.test(([1,4,0,1,6,3,5,2,-4],[3,5,2,8,3,-12],-16),True)
testme.test(([4,-3,2,-5,6,7],[3,5,7],4),True)
testme.test(([5,3,-2,4,-3,2],[10,30,20,-100],50),False)
testme.test(([100,200,300,400],[500,500,600,200],12),False)
