# Complexity is O(log(m*n)) ------> General O(log(N))
import sys
sys.path.append("..")
from BasicTester import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,array,target):
        self.array=array
        self.target=target

def binarySearch(pack):
    left=0
    right=len(pack.array[0])*len(pack.array)-1
    while(left<=right):
        middle=(left+right)//2
        cx=middle%len(pack.array[0])
        rx=(middle-cx)//len(pack.array[0])
        if(pack.array[rx][cx]>pack.target):
            right=middle-1
        elif(pack.array[rx][cx]<pack.target):
            left=middle+1
        if(pack.array[rx][cx]==pack.target):
            return True
    return False

testme=BasicTester(binarySearch)
testme.test(packet([[1,2,3,4],[8,9,10,11],[13,15,17,19]],13),True)
testme.test(packet([[1,2,3,4],[8,9,10,11],[13,15,17,19]],20),False)
testme.test(packet([[1,2,3,4],[8,9,10,11],[13,15,17,19]],19),True)
testme.test(packet([[1,2,3],[34,56,78],[90,112,333]],13),False)
