import sys
sys.path.append("..")
from BasicTester import BasicTester

def find(array):
   return ( sum(array)-sum(set(array)) )//(len(array)-len(set(array)) )

tester=BasicTester(find)
tester.test([1,1,3,4,1,9,5],1)
tester.test([4,3,1,5,3,2,2],2)
tester.test([3,2,1,4,3,6,7],3)
