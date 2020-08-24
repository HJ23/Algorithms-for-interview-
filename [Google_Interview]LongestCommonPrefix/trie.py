class Node:
   def __init__(self):
      self.map={}
      self.completed=False
      self.counter=0

class Trie:
   def __init__(self):
      self.root=Node()
   def add(self,word):
      current=self.root
      for i,x in enumerate(word):
         if(not x in current.map):
            current.map[x]=Node()
         current=current.map[x]
         current.counter+=1
      current.completed=True
   def get(self,word):
      current=self.root
      for i,x in enumerate(word):
         if(not x in current.map):
            return False
         current=current.map[x]
      return current.completed

   def getLongestPrefix(self):
      queue=[(self.root,"")]
      maxi=(0,"")
      while(len(queue)!=0):
         node,tmp=queue.pop(0)
         for x in node.map.items():
            if(node.counter>=maxi[0] and len(tmp)>len(maxi[1]) ):
               maxi=(node.counter,tmp)
            queue.append((x[1],tmp+x[0]))

      return maxi


tr=Trie()
tr.add("apple")
tr.add("app")
tr.add("apple")
tr.add("banana")
tr.add("banan")
tr.add("bananashake")

print(tr.getLongestPrefix())
