# Complexity is O(n)

from BasicTester import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,array,k):
        self.array=array
        self.k=k


def run(pack):
    hashmap={}
    for item in pack.array:
        hashmap[item]=[] #Stack for each character
    for index in range(len(pack.array)):
        if(len(hashmap[pack.array[index]])!=0):
            if((index-hashmap[pack.array[index]][-1])<=pack.k):
                return True
        hashmap[pack.array[index]].append(index)
    return False

testme=BasicTester(run)
testme.test(packet([1,2,3,4,5,6,3,8],5),True)
testme.test(packet([1,2,3,4,5,6,3,8],4),True)
testme.test(packet([1,2,3,4,5,6,3,8],3),False)
testme.test(packet([8,2,22,4,5,6,3,8],2),False)
testme.test(packet([8,2,22,4,5,6,3,8],8),True)
