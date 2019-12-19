import sys
sys.path.append("..")
from BasicTester import BasicTester


def maxSubArray(nums: [int]) -> int:
    sum=0
    max=nums[0]
    for x in range(0,len(nums)):
        sum+=nums[x]
        if(sum<nums[x]):
            sum=nums[x]
        if(sum>max):
            max=sum
    return max

testme=BasicTester(maxSubArray)
testme.test([-1,2,3,-4,5,-1,2,4],11)
testme.test([-1,-2,-3,-4,-5,-6],-1)
testme.test([-1,2,-3,4,-5,6,-7,-8,10],10)
testme.test( [-2,1,-3,4,-1,2,1,-5,4],6)