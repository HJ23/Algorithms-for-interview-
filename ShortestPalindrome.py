#  Shortest Palindrome 
#  Complexcity O(n) for both cases

import os

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

def spalindrome(string):
   pass

right=rightPass("aabcd")
left=  leftPass("aabcd")

if(len(right)<len(left)):
   print(right)
else:
   print(left)
