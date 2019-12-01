# Complexity is O(n)
import sys
sys.path.append("..")
from BasicTester import BasicTester

def run(arg):
    stack=[]
    coord=[]
    for index in range(0,len(arg)):
        if(arg[index]=="("):
            stack.append("(")
            coord.append(index)
        elif(arg[index]==")"):
            if(len(stack)==0):
                coord.append(index)
            else:
                stack.pop()
                coord.pop()
    coord=set(coord)
    result1=""
    for index in range(0,len(arg)):
        if(not index in coord):
            result1+=arg[index]
    return result1

testme=BasicTester(run)
testme.test("((())","(())")
testme.test("())","()")
testme.test("(((","")
