import sys
sys.path.append("..")
from BasicTester import *


def add(val):
   a,b=val
   maxi=a if(len(a)>len(b)) else b
   mini=a if(len(a)<=len(b)) else b
   maxi=maxi[::-1]
   mini=mini[::-1]
   reminder=0
   ret=""
   for x in range(len(mini)):
      tmp=reminder+int(mini[x])+int(maxi[x])
      ret=str(tmp%10)+ret
      reminder=tmp//10
   if(reminder==0):
      ret=maxi[len(mini):len(maxi)][::-1]+ret
   else:
      for x in range(len(mini),len(maxi)):
         tmp=reminder+int(maxi[x])
         ret=str(tmp%10)+ret
         reminder=tmp//10
      if(reminder!=0):
         ret=str(reminder)+ret
   return ret

tester=BasicTester(add)
tester.test(("12","23"),"35")
tester.test(("998","0"),"998")
tester.test(("999","99"),"1098")
tester.test(("0","120"),"120")
