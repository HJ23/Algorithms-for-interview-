# Complexity is O(max(n,m)) ---> O(N)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import copy
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp=None
        first=None
        reminder=0
        list=[]
        while(l1!=None and l2!=None):
            sum=reminder+l1.val+l2.val
            reminder=1 if(sum>=10) else 0
            sum=sum%10
            if(first==None):
                tmp=ListNode(sum)
                first=tmp
            else:
                abc=ListNode(sum)
                tmp.next=abc
                tmp=abc
            l1=l1.next
            l2=l2.next
        while(l1!=None):
            sum=reminder+l1.val
            reminder=1 if(sum>=10) else 0
            sum=sum%10
            abc=ListNode(sum)
            tmp.next=abc
            tmp=abc
            l1=l1.next
        while(l2!=None):
            sum=reminder+l2.val
            reminder=1 if(sum>=10) else 0
            sum=sum%10
            abc=ListNode(sum)
            tmp.next=abc
            tmp=abc
            l2=l2.next
        if(reminder!=0):
            abc=ListNode(reminder)
            tmp.next=abc
        return first
