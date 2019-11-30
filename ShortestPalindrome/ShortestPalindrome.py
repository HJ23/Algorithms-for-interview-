#  Shortest Palindrome 
#  Complexcity O(n) for both cases
import sys
sys.path.append("..")
from BasicTester import BasicTester

def rightPass(string):
   left=0
   right=len(string)-1
   temp=""
   while(left<right):
      if(string[right]!=string[left]):
         temp=string[left]+temp
         left+=1
      else:
         left+=1
         right-=1
   return string+temp

def leftPass(string):
   string=string[::-1]
   return rightPass(string)

def palindrome(string):
   right=rightPass(string)
   left=  leftPass(string)
   if(len(right)<len(left)):
       return right
   else:
       return left

testme=BasicTester(palindrome)
testme.test("abcde","edcbabcde")

