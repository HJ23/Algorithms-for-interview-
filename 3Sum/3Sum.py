# Complexity O(n^2) --> amortized
import sys
sys.path.append("..")
from BasicTester import BasicTester

class Sum3():
    def __init__(self):
        self.hashmap={}
        self.valueSet=set()
        
    def addSet(self,values):
        temp=tuple(sorted(values))
        self.valueSet.add(temp)

    def check(self,item,x,y):
        result=False
        if((-item in self.hashmap) and result!=x and result!=y):
            result=True
        return result

    def find(self,array):
        for index in range(len(array)):
            self.hashmap[array[index]]=index
        
        for x in range(0,len(array)):
            for y in range(x+1,len(array)):
                a=array[x]+array[y]
                if(self.check(a,x,y)):
                    self.addSet([array[x],array[y],-a])
        return self.valueSet

sum=Sum3()
testme=BasicTester(sum.find)
testme.test([1,2,3,4,1,2,-5],{(-5,2,3),(-5,1,4)})
sum.__init__()
testme.test([1,2,3,4,1,2],set())
  
