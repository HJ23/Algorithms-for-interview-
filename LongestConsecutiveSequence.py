# Complexity O(n)
from . import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,array):
        self.array=array
    def __repr__(self):
        return self.array

def find(pack):
    hashmap={}
    temp=[]
    for item in pack.array:
        hashmap[item]=item
    for item in pack.array:
        if(item+1 in hashmap):
            temp.append(item+1)
        if(item-1 in hashmap):
            temp.append(item-1)
    return set(temp)

testme=BasicTester(find)
testme.test(packet([56,78,2,90,12,34,1,3,56,38,4]),{1,2,3,4})
testme.test(packet([56,78,90,12,58,3,57,38]),{56,57,58})
testme.test(packet([56,101,90,12,34,102,56,38,4]),{101,102})
