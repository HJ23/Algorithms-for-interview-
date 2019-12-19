import sys
sys.path.append("..")
from BasicTester import BasicTester,argumentPack

class pack(argumentPack):
    def __init__(self,array,pattern):
        self.array=array
        self.pattern=pattern

def findPattern(packet):
    ret=[]
    for x in packet.array:
        if(len(packet.pattern)!=len(x)):
            continue
        hashmap1={}
        hashmap2={}
        yes=True
        for index in range(0,len(x)):
            if(x[index] in hashmap1):
                if(hashmap1[x[index]]!=packet.pattern[index]):
                    yes=False
                    break
            if((packet.pattern[index] in hashmap2)):
                if(hashmap2[packet.pattern[index]]!=x[index]):
                    yes=False
                    break
            else:
                hashmap2[packet.pattern[index]]=x[index]
                hashmap1[x[index]]=packet.pattern[index]
        if(yes):
            ret.append(x)
    return ret

testme=BasicTester(findPattern)
testme.test(pack(["abb","maa","cbb","abh","asas"],"ghh"),["abb","maa","cbb"])
testme.test(pack(["aaa","bbb","abc","edf"],"ghh"),[])
testme.test(pack(["abb","399","211","121","asasass","bvv"],"abb"),["abb","399","211","bvv"])
