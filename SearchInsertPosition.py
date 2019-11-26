# Complexity O(log(n))
from BasicTester import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,array,target):
        self.array=array
        self.target=target
    def getArray(self):
        return self.array
    def getTarget(self):
        return self.target
    
def binarySearch(packet):
    left=0
    right=len(packet.array)-1
    while(left<right):
        middle=int((left+right)/2)
        if(packet.array[middle]==packet.target):
            break
        if(packet.array[middle]>packet.target):
            middle-=1
            right=middle
        elif(packet.array[middle]<packet.target):
            middle+=1
            left=middle
    return middle

def find(packet):
    index=binarySearch(packet)
    if(packet.target>packet.array[index]):
        return index+1
    else:
        return index
    
testme=BasicTester(find)
testme.test(packet([1,2,3,4,7,120,121],100),5)