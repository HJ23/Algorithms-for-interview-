class Node:
   def __init__(self,val,next=None):
      self.val=val
      self.next=next

class LinkedList:
   def __init__(self):
      self.root=None
      self.curr=None
   def add(self,val):
      if(not self.root):
         self.root=Node(val)
         self.curr=self.root
      else:
         self.curr.next=Node(val)
         self.curr=self.curr.next


def add(l1,l2):
   ret=None
   memory=None
   reminder=0
   while(l1 and l2):
      sum=reminder+l1.val+l2.val
      if(memory==None):
         memory=Node(sum%10)
         ret=memory
      else:
         memory.next=Node(sum%10)
         memory=memory.next
      reminder=sum//10
      l1=l1.next
      l2=l2.next
   l1=l1 if(l1) else l2
   while(l1):
      sum=l1.val+reminder
      memory.next=Node(sum%10)
      memory=memory.next
      reminder=sum//10
      l1=l1.next
   if(reminder!=0):
      memory.next=Node(1)
   return ret

def printll(root):
   ret=""
   while(root):
      ret+=str(root.val)+" "
      root=root.next
   print(ret)

l1=LinkedList() # 165
l1.add(5)
l1.add(6)
l1.add(1)

l2=LinkedList() # 29
l2.add(9)
l2.add(2)


printll(add(l1.root,l2.root))



