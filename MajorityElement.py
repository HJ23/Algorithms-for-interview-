# Complexity is O(N) amortized

from BasicTester import BasicTester,argumentPack

def run(array):
    hashmap={}
    result=[]
    for item in array:
        hashmap[item]=0
    for item in array:
        hashmap[item]+=1
    for item in hashmap:
        if(hashmap[item]>=len(array)/2):
            result.append(item)
    return result

testme=BasicTester(run)
testme.test([1,4,7,23,21,1,12,2,2,2,2,2,2,2,2],[2])
testme.test([2,2,2,3,3,3],[2,3])
testme.test([1,2,3,4,5,6,7],[])
testme.test([1,2,3,1,2,3,1,2,3,1,2,3],[])










