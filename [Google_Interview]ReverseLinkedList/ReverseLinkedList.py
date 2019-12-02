
class node():
    def __init__(self,element):
        self.element=element
        self.next=None
    def next(self,nextNode):
        self.next=nextNode
class LinkedList():
    __head=None
    __current=None
    def add(self,element):
        temp=node(element)
        if(self.__head==None):
            self.__head=temp
            self.__current=self.__head
        else:
            self.__current.next=temp
            self.__current=self.__current.next
    def __repr__(self):
        temp=""
        tempNode=self.__head
        while(tempNode!=None):
            temp+=str(tempNode.element)+"->"
            tempNode=tempNode.next
        return temp
    def prt(self,number):
        tempNode=self.__head
        for x in range(0,number):
            if(tempNode==None):
                break
            else:
                tempNode=tempNode.next
        return tempNode
    def REVERSE(self):
        prv=None
        current=self.__head
        while(current!=None):
            temp=current.next
            current.next=prv
            prv=current
            current=temp
        self.__head=prv

ll=LinkedList()
ll.add(56)
ll.add(67)
ll.add(89)
ll.add(6)
print(ll)
ll.REVERSE()
print(ll)