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
    sorted_x = sorted(map.items(), key=lambda kv: kv[1],reverse=True)
    oddd=False
    for key in sorted_x:
        if(key[1]%2==0):
            maximum+=key[1]
        else:
            if(oddd is False):
                oddd=True
                maximum+=key[1]
            else:
                maximum+=key[1]-1
    return maximum

testme=BasicTester(find)
testme.test("abccccddk",7)
testme.test("abc",1)
testme.test("abccc",3)
testme.test("aAAAAA",5)
testme.test("123321",6)
testme.test("",0)



