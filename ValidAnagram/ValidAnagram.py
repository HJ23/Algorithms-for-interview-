import sys
sys.path.append("..")
from BasicTester import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,str1,str2):
        self.string1=str1
        self.string2=str2

def isAnagram(pack:packet) -> bool:    
    if(len(pack.string1)!=len(pack.string2)):
        return False
    hashmap={}
    for x in pack.string1:
        if(x in hashmap):
            hashmap[x]+=1
        else:
            hashmap[x]=1        
    for x in pack.string2:
        if(not x in hashmap):
            return False
        elif(hashmap[x]==0):
            return False
        else:
            hashmap[x]-=1    
    return True

testme=BasicTester(isAnagram)
testme.test(packet("abcdfffggf","abchdf"),False)
testme.test(packet("abc","cba"),True)
testme.test(packet("aaabb","aabbb"),False)
testme.test(packet("ppale","apple"),True)
