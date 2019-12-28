import sys
sys.path.append("..")
from BasicTester import BasicTester 

class ListNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def find(root):
    queue=[root]
    sum=0        
    while(len(queue)!=0):
        node=queue[0]
        queue.pop(0)
        
        if(node!=None and node.left!=None and node.left.left==None and node.left.right==None):
            sum+=node.left.val
            queue.append(node.right)
        elif(node!=None):
            queue.append(node.right)
            queue.append(node.left)        
    return sum

testme=BasicTester(find)

root=ListNode(1)
root.left=ListNode(2)
root.right=ListNode(3)
root.left.left=ListNode(4)
root.left.right=ListNode(5)

root1=ListNode(3)
root1.left=ListNode(9)
root1.right=ListNode(20)
root1.right.left=ListNode(15)
root1.right.right=ListNode(7)

testme.test(root,4)
testme.test(root1,24)
testme.test(ListNode(3),0)
testme.test(ListNode(None),0)