import sys
sys.path.append("..")
from BasicTester import BasicTester

class hset:
   def __init__(self):
      # 1000000//10000
      self.mem=[[] for _ in range(10000) ]
   def add(self,key):
      if(not key in self.mem[key%10000]):
         self.mem[key%10000].append(key)
   def remove(self,key):
      for i,x in enumerate(self.mem[key%10000]):
         if(x==key):
            del self.mem[key%10000][i]
            return
   def contains(self,key):
      return True if(key in self.mem[key%10000]) else False


set=hset()
testme=BasicTester(set.contains)
set.add(12)
set.add(34)
set.add(33)
set.add(65)
set.add(12)
set.add(65)
testme.test(12,True)
set.remove(12)
testme.test(12,False)
set.remove(65)
set.remove(65)
set.remove(33)
testme.test(65,False)
