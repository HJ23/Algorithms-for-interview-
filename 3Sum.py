# Complexity O(n^2) --> amortized
from BasicTester import *

class Summer():
   def addSet(coordinates):
      coordinates=sorted(coordinates)
      temp=tuple(coordinates)
      valueSet.add(temp)

   def check(item,x,y):
       result=None
       if(-item in hashmap):
           result=hashmap[-item]
           result=None if(result==x) else None if(result==y) else result
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
    return ValueSet
find(array)
          
    
    
