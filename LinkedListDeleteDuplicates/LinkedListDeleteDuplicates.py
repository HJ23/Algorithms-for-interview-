# Complexity is Time : O(n) Space : O(1)
class Node:
    def __init__(self,value):
        self.value=value
        self.nextNode=None
    def setNext(self,node):
        self.nextNode=node
    def getNext(self):
        return self.nextNode

class LinkedList():
    def __init__(self):
        self.head=None
        self.current=None
    def add(self,value):
        tempNode=Node(value)
        if(self.head==None):
            self.head=tempNode
            self.current=self.head
        else:
            self.current.setNext(tempNode)
            self.current=tempNode
    def __repr__(self):
        temp=""
        tempNode=self.head
        while(tempNode!=None):
            temp+=str(tempNode.value)+","
            tempNode=tempNode.getNext()
        return temp
    def deleteDuplicates(self):
        i=self.head
        j=self.head.getNext()
        while(j.getNext()!=None):
            if(j.value!=i.value):
                i.setNext(j)
                i=j
            j=j.getNext()
        if(i.value==j.value):
            i.setNext(j.getNext())
        
ll=LinkedList()
ll.add(1)
ll.add(1)
ll.add(5)
ll.add(5)
ll.add(5)
ll.add(6)
ll.add(6)
ll.add(6)
ll.add(6)
ll.add(6)

ll.deleteDuplicates()
print(ll)
        
