# Complexity General : O(m*n)  -------> m is lenght of minimum sized string in given array
# Best Case  : O(n)
# Worst Case : O(n^2)
import sys
sys.path.append("..")
from BasicTester import BasicTester,argumentPack

class packet(argumentPack):
    def __init__(self,array):
        self.array=array
    def getArray(self):
        return self.array

def run(pack):
    minString=pack.array[0]
    memory=[]
    result=""
    for item in pack.array:
        if(len(minString)>len(pack.array)):
            minString=item
    for _ in range(len(minString)):
        memory.append(0)
    
    for index in range(len(minString)):        
        for item in pack.array:
            if(item[index]==minString[index]):
                memory[index]+=1
        if(memory[index]==len(pack.array)):
            result=minString[0:index+1]
        else:
            break
    return result

testme=BasicTester(run)
testme.test(packet(["abcsssss","abcdef","abcd","abcdddddddd"]),"abc")
testme.test(packet(["abc","asasas","abcd","12122"]),"")
testme.test(packet(["abc","asd","defrttt","defr"]),"")
testme.test(packet(["a","as","abc","abcdefg"]),"a")
testme.test(packet(["abcdefr11","abcdef22r","abcd22efr","abcde33fr"]),"abcd")



