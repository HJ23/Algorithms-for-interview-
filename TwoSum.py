# Complexity O(n)
import os

array=[2,7,11,15,16,27,38,39]
target=54

def twoSum(array,sum):
    i=0
    j=len(array)-1
    while(j>i):
        if((array[i]+array[j])>sum):
            j-=1
        elif((array[i]+array[j])<sum):
            i+=1
        else:
            print(str(array[i])+" "+str(array[j]))
            break
    
twoSum(array,target)

