# Complexity is O(n)
import sys
sys.path.append("..")
from BasicTester import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,array1,array2):
        self.array1=array1
        self.array2=array2

def run(packet):
    long=[]
    short=[]
    long=packet.array1.copy() if(len(packet.array1)>=len(packet.array2)) else packet.array2.copy()
    short=packet.array2.copy() if(len(packet.array1)>=len(packet.array2)) else packet.array1.copy()
    intersection=[]
    hashmap_Arr1={}
    hashmap_Arr2={}
    for index in range(len(short)):
        hashmap_Arr1[short[index]]=short[index]
        hashmap_Arr2[long[index]]=long[index]
        
    for index in range(len(short),len(long)):
        hashmap_Arr2[long[index]]=long[index]
        
    for item in hashmap_Arr1:
        if(item in hashmap_Arr2):
            intersection.append(item)
    return intersection

testme=BasicTester(run)
testme.test(packet([1,2,34,5,8,99,0],[0,1,90]),[0,1])
testme.test(packet([1,2,34,5,8,99,143],[0,1,9990,12,143,89]),[1,143])
testme.test(packet([1,2,34,5,8,99,0],[13,14,15]),[])
testme.test(packet([1,2,34,5,8,99,0],[0]),[0])
testme.test(packet([1,2,34,5,8,99,0],[]),[])
    