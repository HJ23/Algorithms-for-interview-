import sys
sys.path.append("..")
from BasicTester import BasicTester


def romanToInt(string: str) -> int:
    hashmap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    size=len(string)
    sum=0
    for x in range(0,size-1):
        if(hashmap[string[x]]>=hashmap[string[x+1]]):
            sum+=hashmap[string[x]]
        elif(hashmap[string[x]]<hashmap[string[x+1]]):
            sum-=hashmap[string[x]]
            
    sum+=hashmap[string[size-1]]
    return sum

testme=BasicTester(romanToInt)
testme.test("VIII",8)
testme.test("MMMDCCXXIV",3724)
testme.test("DCC",700)
testme.test("IIIVIII",9)
testme.test("V",5)
