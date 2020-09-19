import sys
sys.path.append("..")
from UniTest import *


def sol1(arr):
   ret=set()
   for p,x in enumerate(arr):
      i=p
      j=len(arr)-1
      while(i<j):
         tmp=x+nums[i]+nums[j]
         if(tmp>0):
            j-=1
         elif(tmp<0):
            i+=1
         else:
            if(i!=j and i!=p and j!=p):
               ret.add(tuple(sorted((arr[i],arr[j],x))))
   return list(ret)
