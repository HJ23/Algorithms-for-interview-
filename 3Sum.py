# Complexity O(n^2) --> amortized

# a+b+c=0
# -a=(b+c)
import os


array=[1,4,9,-2,-5,7] # random array unsorted
hashmap={}
valueSet=set()

# constant time sorting
def addSet(coordinates):
    global valueSet
    coordinates=sorted(coordinates)
    temp=tuple(coordinates)
    valueSet.add(temp)

def check(item,x,y):
    result=None
    try:
        result=hashmap[-item]
        if(result==x or result==y):
            result=None
    except:
        pass
    return result

def find(array):
    global valueSet
    for index in range(len(array)):
        hashmap[array[index]]=index
        
    for x in range(len(array)):
        for y in range(len(array)):
            if(x==y):
                continue
            a=array[x]+array[y]
            if(check(a,x,y)!=None):
                addSet([array[x],array[y],-a])
    print(valueSet)
find(array)
          
    
    