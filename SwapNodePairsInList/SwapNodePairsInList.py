class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        tmp_str=str(self.val)+" "
        tmp=self.next
        while(tmp!=None):
            tmp_str+=str(tmp.val)+" "
            tmp=tmp.next
        return tmp_str

def swapPairs(head: ListNode) -> ListNode:
    first=True
    tmp=head
    pre=None
    while(tmp!=None):
        if(tmp.next!=None):
            p=tmp.next.next
            k=tmp.next
            tmp.next=p
            k.next=tmp
            if(first):
                head=k
                first=False
            else:
                pre.next=k   
        else:
            break
        pre=tmp
        tmp=p
    return head
