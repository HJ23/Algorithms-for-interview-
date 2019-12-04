# Complexity is Time: O(n)  Space: O(1)
# *For Doubly LinkedList

import sys
sys.path.append("..")
from BasicTester import BasicTester

class Node:
    def __init__(self,value):
        self.value=value
        self.nextNode=None
        self.prvNode=None
    def next(self,_nextNode_):
        self.nextNode=_nextNode_
    def previous(self,_prvNode_):
        self.prvNode=_prvNode_
    def getValue(self):
        return self.value
    def getNext(self):
        return self.nextNode
    def getPrv(self):
        return self.prvNode
    
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
            tempNode.previous(self.current)
            self.current.next(tempNode)
            self.current=tempNode
    def __repr__(self):
        temp=""
        current=self.head
        while(current!=None):
            temp+=str(current.getValue())+"->"
            current=current.getNext()
        return temp
    def isPalindrome(self):
        rabbit=self.head
        tortoise=self.head
        while(True):
            if(rabbit.getNext()==None):
                break
            if(rabbit.getNext().getNext()==None):
                rabbit=rabbit.getNext()
                break
            else:
                rabbit=rabbit.getNext().getNext()
                tortoise=tortoise.getNext()
        head1=self.head
        head2=rabbit
        while(head2!=tortoise):
            if(head1.getValue()!=head2.getValue()):
                return False
            head1=head1.getNext()
            head2=head2.getPrv()
        return True
        
testLL1=LinkedList()
testLL1.add(45)
testLL1.add(478)
testLL1.add(44)
testLL1.add(55)
testLL1.add(44)
testLL1.add(478)
testLL1.add(45)


testLL2=LinkedList()
testLL2.add(45)
testLL2.add(44)
testLL2.add(55)
testLL2.add(44)
testLL2.add(478)

testme=BasicTester(LinkedList.isPalindrome)
testme.test(testLL1,True)
testme.test(testLL2,False)