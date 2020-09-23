import sys
sys.path.append("..")
from UniTester import *

# central propagation solution

def solve(string):
   maxi=""

   for x in range(0,len(string)):
      tmp=string[x]
      i,j=x-1,x+1
      while(i>=0 and j<len(string)):
         if(string[i]==string[j]):
            tmp=string[i]+tmp+string[j]
            i-=1
            j+=1
         else:
            break
      if(len(maxi)<len(tmp)):
         maxi=tmp
      i,j=x,x+1
      tmp=""
      while(i>=0 and j<len(string)):
         if(string[i]==string[j]):
            tmp=string[i]+tmp+string[j]
            i-=1
            j+=1
         else:
            break
      if(len(tmp)>len(maxi)):
         maxi=tmp
   return maxi

@unitest(target='aaaaaa')
def test1(string='aaaaaa'):
   return solve(string)

@unitest(target='a')
def test2(string='a'):
   return solve(string)

@unitest(target='abba')
def test3(string='dksjdkabbadff5jrrkfggg'):
   return solve(string)

assert test2()
assert test1()
assert test3()
