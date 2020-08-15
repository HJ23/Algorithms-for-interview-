import sys
sys.path.append("..")
from BasicTester import *

def find(val):
   S,T=val
   nums=[x for x in range(len(S))]
   diction={x:y for x,y in zip(list(S),nums)  }
   rev_diction={x:y for x,y in zip(nums,list(S)) }
   
   memory=[]
   temp=[]
   for x in T:
      if(x in diction):
         memory.append(diction[x])
      else:
         temp.append(x)
   memory=list(map(lambda x:rev_diction[x],sorted(memory)))
   for x in temp:
      memory.append(x)
   return "".join(memory)

tester=BasicTester(find)
tester.test(("cbs","scccbs"),"cccbss")
tester.test(("cbnma","dfmnvacb"),"cbnmadfv")
tester.test(("",""),"")
