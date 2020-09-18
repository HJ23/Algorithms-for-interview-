from UniTester.UniTester import *


def find(arr):
   maxi_area=0
   i=0
   j=len(arr)-1
   while(j>i):
      if(arr[i]<arr[j]):
         maxi_area=max(maxi_area,(j-i)*arr[i])
         i+=1
      else:
         maxi_area=max(maxi_area,(j-i)*arr[j])
         j-=1
   return maxi_area

@timer
@unitest(target=4)
def test1(arr):
   return find(arr)

@timer
@unitest(target=49)
def test2(arr):
   return find(arr)



assert  test1([1,2,3,4])
assert  test2([1,8,6,2,5,4,8,3,7])

