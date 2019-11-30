# Complexity O(n)
import os
from BasicTester import BasicTester
query="(((((()))(())"

def validParanthesis(query):
    stack=[]
    counter=0
    for item in query:
        if(item=="("):
            stack.append("(")
        elif(item==")"):
            if(len(stack)!=0):
                stack.pop()
                counter+=1
    return counter
    
testme=BasicTester(validParanthesis)
testme.test(query,5)
testme.test("(((",0)
testme.test("((()))",3)
testme.test("   ((()))",3)




