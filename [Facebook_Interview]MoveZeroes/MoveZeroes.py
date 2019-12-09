#Complexity is O(n)

import sys
sys.path.append("..")
from BasicTester import BasicTester

def moveZeroes(array):
    if(len(array)<=1):
        return array
    i=0
    j=1
    while(True):
        if(array[i]==0 and array[j]!=0):
            array[i]=array[j]
            array[j]=0
        elif(array[i]==0 and array[j]==0 ):
            j+=1
        else:
            i+=1
            j+=1
        if(i==len(array) or j==len(array)):
            break
    return array

testme=BasicTester(moveZeroes)
testme.test([1,0,0,1,2,3],[1,1,2,3,0,0])
testme.test([1,0,1,2,0,2,3,0,3],[1,1,2,2,3,3,0,0,0])
testme.test([1,0],[1,0])
testme.test([0,1],[1,0])
testme.test([0],[0])            