import sys
sys.path.append("..")
from BasicTester import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,array1,array2):
        self.arr1=array1.copy()
        self.arr2=array2.copy()
    

def intersect(pack:packet) -> [int]:
    hashmap1={}
    hashmap2={}
    ret=[]
    for x in pack.arr1:
        if(x in hashmap1):
            hashmap1[x]+=1
        else:
            hashmap1[x]=1
    
    for x in pack.arr2:
        if(x in hashmap2):
            hashmap2[x]+=1
        else:
            hashmap2[x]=1
    
    if(len(hashmap1)>len(hashmap2)):
        for key in hashmap2:
            if(key in hashmap1):
                m=min(hashmap1[key],hashmap2[key])
                for x in range(0,m):
                    ret.append(key)
    else:
        for key in hashmap1:
            if(key in hashmap2):
                m=min(hashmap1[key],hashmap2[key])
                for x in range(0,m):
                    ret.append(key)
    return ret
        
testme=BasicTester(intersect)
testme.test(packet([1,222,2,2,2,4],[2,2,2,2,2,2]),[2,2,2])
testme.test(packet([1,2,3,4,5],[2,2,2,2,2,2]),[2])
testme.test(packet([1,3,6,7,8],[2,4,5]),[])
testme.test(packet([1,2,3,4,5],[1,2,3]),[1,2,3])