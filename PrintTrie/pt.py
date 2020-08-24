class Node:
   def __init__(self):
      self.map={}
      self.completed=False

class Trie:
   def __init__(self):
      self.root=Node()
   def add(self,word):
      current=self.root
      for i,x in enumerate(word):
         if(not x in current.map):
            current.map[x]=Node()
         current=current.map[x]
      current.completed=True
   def get(self,word):
      current=self.root
      for i,x in enumerate(word):
         if(not x in current.map):
            return False
         current=current.map[x]
      return current.completed

   def __repr__(self):
      ret=[]
      queue=[(self.root,"")]
      while(len(queue)!=0):
         node,tmp=queue.pop(0)
         if(node.completed):
            ret.append(tmp)
         for x in node.map.items():
            queue.append((x[1],tmp+x[0]))
      return str(ret)

tr=Trie()
tr.add("apple")
tr.add("app")
tr.add("banana")
tr.add("word")
tr.add("appp")
print(tr)
