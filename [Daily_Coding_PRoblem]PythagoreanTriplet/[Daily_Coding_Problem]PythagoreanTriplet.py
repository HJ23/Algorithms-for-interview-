import math
import sys
sys.path.append("..")
from BasicTester import BasicTester

def run(array):
    hashSet=set()
    for item in array:
        hashSet.add(item)
    for a in array:
        for b in array:
            if(a==0 or b==0):
                continue
            cSquare=a*a+b*b
            c=math.sqrt(cSquare)
            if((c-int(c))==0 and c in hashSet):
                print(str(a)+" "+str(b)+" "+str(c))
                return True
    return False

testme=BasicTester(run)
testme.test([12,13,2,3,34,5,33,33,4],True)
testme.test([12,13,4],False)
testme.test([0,12,1,2],False)
