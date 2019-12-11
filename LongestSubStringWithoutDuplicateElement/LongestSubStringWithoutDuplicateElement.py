import sys
sys.path.append("..")
from BasicTester import BasicTester

def find(string:str)->int:
    leng=len(string)
    if(leng==0):
        return 0
    _set=set()
    hashmapCord={}
    maxX=0
    maxY=0
    start=0
    
    for x in range(0,leng):
        hashmapCord[string[x]]=[]
    
    for x in range(0,leng):
        if(string[x] in _set):
            if(start<=hashmapCord[string[x]][0]):
                start=hashmapCord[string[x]][0]+1
                hashmapCord[string[x]].pop(0)
                hashmapCord[string[x]].append(x)
            elif(start>hashmapCord[string[x]][0]):
                hashmapCord[string[x]].pop(0)
                hashmapCord[string[x]].append(x)                
        else:
            _set.add(string[x])
            hashmapCord[string[x]].append(x)
        if((x-start)>(maxY-maxX)):
            maxY=x
            maxX=start
    return (maxY-maxX+1)

testme=BasicTester(find)
testme.test("abbbbccccdeeeeefghjl",6)
testme.test("aaaaaaaaaaaaa",1)
testme.test("abcdabcdefghtj",10)
testme.test("",0)

