import sys
sys.path.append("..")
from BasicTester import *

def find(var):
   s,d=var
   ret=[]
   for word in d:
      i=0
      for letter in s:
         if(letter==word[i]):
            i+=1
            if(len(word)==i):
               ret.append(word)
               break
   if(len(ret)==0):
      return ""
   maximum=len(max(ret,key=lambda x:len(x)))
   filtered=list(filter(lambda x:len(x)==maximum,ret))

   return sorted(filtered)[0]

tester=BasicTester(find)
tester.test(("abcmkkoeeneey",["apple","money","mkk"]),"money")
tester.test(("abpcplea",["ale","apple","monkey","plea"]),"apple")
tester.test(("abpcplea",["a","b","c"]),"a")
