class Node:
   def __init__(self,val):
      self.val=val
      self.next=None


class LinkedList:
   def __init__(self):
      self.head=None
      self.current=None
   def add(self,val):
      if(self.head==None):
         self.head=Node(val)
         self.current=self.head
      else:
         self.current.next=Node(val)
         self.current=self.current.next
   def __repr__(self):
      tmp=self.head
      ret=""
      while(tmp!=None):
         ret=ret+"->"+str(tmp.val)
         tmp=tmp.next
      return ret

def removeElements(head: list, val: int):
   prv=None
   tmp=head
   while(tmp!=None):
      if(tmp.val==val and prv==None):
         tmp=tmp.next
         head=tmp
      else:
         if(tmp.val==val):
            prv.next=tmp.next
            tmp=prv.next
         else:
            prv=tmp
            tmp=tmp.next
   return head

ll=LinkedList()
ll.add(12)
ll.add(13)
ll.add(56)
ll.add(23)
ll.add(13)

removeElements(ll.head,13) # inplace changed
print(ll)
