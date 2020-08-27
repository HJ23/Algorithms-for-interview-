import sys
sys.path.append("..")
from BasicTester import *

def remove(string):
   tmp=[]
   string=list(string)
   for x in string:
      if(len(tmp)==0):
         tmp.append(x)
      elif(tmp[-1]==x):
         tmp.pop(-1)
      else:
         tmp.append(x)
   return "".join(tmp)

tester=BasicTester(remove)
tester.test("aabbcdaa","cd")
tester.test("bbbcdv","bcdv")
tester.test("aaaaaa","")
