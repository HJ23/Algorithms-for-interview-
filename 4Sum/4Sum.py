import sys
sys.path.append("..")
from BasicTester import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,array,target):
        self.array=array
        self.target=target

def find(pack):
    if(len(pack.array)<4):
        return []
    hashmap={}
    result=set()
    for count,element in enumerate(pack.array):
        if(not element in hashmap):
            hashmap[element]=1
        else:
            hashmap[element]+=1
    size=len(pack.array)
    for x in range(0,size):
        for y in range(x+1,size):
            for z in range(y+1,size):
                c=pack.target-(pack.array[x]+pack.array[y]+pack.array[z])
                if(c in hashmap):
                    sss=0
                    if(pack.array[x]==c):
                        sss+=1
                    if(pack.array[y]==c):
                        sss+=1
                    if(pack.array[z]==c):
                        sss+=1
                    if(sss+1<=hashmap[c]):
                        result.add(tuple(sorted([pack.array[x],pack.array[y],pack.array[z],c])))
    return result

testme=BasicTester(find)
testme.test(packet([0,-1,2,-1,0],0),{(-1,-1,0,2)})
testme.test(packet([0,-1,2,2,3,-5,-1,0],0),{(-5,0,2,3),(-1,-1,0,2)})
testme.test(packet([0,-1,2,-1,0],-2),{(-1,-1,0,0)}) 