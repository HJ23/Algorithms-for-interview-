# Time Complexity is O(N)
# Memory Complexity is O(N)

import sys
sys.path.append("..")
from BasicTester import BasicTester

def find(input:str)->int:
    maximum=0
    map={}
    for x in input:
        if(x in map):
            map[x]+=1
        else:
            map[x]=1
    sort= sorted(map.values(),reverse=True)
    oddd=False
    for val in sort:
        if(val%2==0):
            maximum+=val
        else:
            oddd=True
            maximum+=val-1
    return maximum+oddd

testme=BasicTester(find)
testme.test("abccccddk",7)
testme.test("abc",1)
testme.test("abccc",3)
testme.test("aAAAAA",5)
testme.test("123321",6)
testme.test("",0)



