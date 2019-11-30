from BasicTester import BasicTester

class packet():
    def __init__(self,array,k):
        self.array=array
        self.k=k
    def getArray(self):
        return self.array.copy()
    def getK(self):
        return self.k


def run(pack):
    hashmap={}
    for item in pack.array:
        if(not item in hashmap):
            hashmap[item]=1
        else:
            hashmap[item]+=1
    for item in hashmap:
        if(hashmap[item]==pack.k):
            return True
    return False

testme=BasicTester(run)
testme.test(packet([1,1,1,2,2,2,2,3,3,3],3),True)
testme.test(packet([1,1,1,2,2,2,2,3,3,3,3,3],5),True)
testme.test(packet([1,1,1,2,2,2,2,3,3,3],10),False)
testme.test(packet([1],2),False)


