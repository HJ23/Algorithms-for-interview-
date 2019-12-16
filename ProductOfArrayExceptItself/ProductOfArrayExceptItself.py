
import sys
sys.path.append("..")
from BasicTester import BasicTester

def productExceptSelf(nums: [int]) -> [int]:
    left_right=[]
    right_left=[]
    tmp=1
    for num in nums:
        tmp*=num
        left_right.append(tmp)
    tmp=1
    for num in nums[::-1]:
        tmp*=num
        right_left.append(tmp)
    res=[]
    res.append(right_left[-2])
    for x in range(0,len(nums)-2):
        res.append(   left_right[x] * right_left[len(nums)-x-3])
    res.append(left_right[-2])
    return res

testme=BasicTester(productExceptSelf)
testme.test([2,3,4,5,6,7,8],[20160,13440,10080,8064,6720,5760,5040])
testme.test([1,2,3,4],[24,12,8,6])

