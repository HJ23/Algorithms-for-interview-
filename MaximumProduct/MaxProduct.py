import sys
sys.path.append("..")

from  BasicTester import BasicTester


def maxProduct(nums) -> int:
   loc_max=1
   tmp=[]
   for x in nums:
      loc_max*=x
      if(x==0):
         loc_max=1
         tmp.append(0)
      else:
         tmp.append(max(loc_max,x))

   loc_max=1
   for x in nums[::-1]:
      loc_max*=x
      if(x==0):
         loc_max=1
         tmp.append(0)
      else:
         tmp.append(max(loc_max,x))
   return max(tmp)


testme=BasicTester(maxProduct)
testme.test([-1,-2,-3,0,12,2],24)
testme.test([-1,2,23,0,3,-4,-34],408)
testme.test([-2,-3,-1,0,0,-4,23,],23)
