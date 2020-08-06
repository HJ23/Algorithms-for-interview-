import sys
sys.path.append("..")
from BasicTester import BasicTester


def find(var):
   arr,target=var
   arr=sorted(arr)
   res=1000000  # max number
   for x in range(len(arr)):
      i=x+1
      j=len(arr)-1
      while(i<j):
         tmp=arr[x]
         tmp+=arr[i]+arr[j]
         if(abs(res-target)>abs(tmp-target)):
            res=tmp
         if(tmp<target):
            i+=1
         elif(tmp>target):
            j-=1
         else:
            return tmp
   return res


testme=BasicTester(find)
testme.test(([-1,2,1,-4],1),2)
testme.test(([0,0,1,1,1,1],1),1)
testme.test(([-1,3,-4,2,1,0,0,0],0),0)
