import sys
sys.path.append("..")
from BasicTester import BasicTester

class map:
   def __init__(self):
      # 1000000//10000
      self.mem=[[] for _ in range(10000)]
   def put(self,key,value):
      for i,x in enumerate(self.mem[key%10000]):
         if(x[0]==key):
            self.mem[key%10000][i]=[key,value]
            return
      self.mem[key%10000].append([key,value])
   def remove(self,key):
      for i,x in enumerate(self.mem[key%10000]):
         if(x[0]==key):
            del self.mem[key%10000][i]
            return
   def get(self,key):
      for i,x in enumerate(self.mem[key%10000]):
         if(x[0]==key):
            return x[1]
      return -1

mymap=map()
testme=BasicTester(mymap.get)
mymap.put(12,23)
mymap.put(1222,33)
mymap.put(100013,22341)
testme.test(12,23)
mymap.remove(12)
testme.test(12,-1)
testme.test(1222,33)
mymap.remove(1222)
mymap.remove(1222)
testme.test(1222,-1)
