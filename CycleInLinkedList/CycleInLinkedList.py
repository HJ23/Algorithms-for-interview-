
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def detectCycle(self, head):
        hset=set()
        while(head!=None):
            if(head in hset):
                return head
            else:
                hset.add(head)
                head=head.next
        return None
    
linked_list1=ListNode(12)
linked_list1.next=ListNode(34)
linked_list1.next.next=ListNode(45)
linked_list1.next.next.next=ListNode(90)
linked_list1.next.next.next.next=linked_list1.next  # node which has value 34 has cycle 
val1=linked_list1.detectCycle(linked_list1).val
print(val1)

linked_list2=ListNode(1)
linked_list2.next=ListNode(2)
linked_list2.next.next=ListNode(3)
linked_list2.next.next.next=ListNode(4)
linked_list2.next.next.next.next=linked_list2.next.next  # node which has value 3 has cycle
val2=linked_list2.detectCycle(linked_list2).val
print(val2)

