import sys
sys.path.append("..")
from BasicTester import *

# not best solution
def solve1(var):
   A,B=var
   dict1={x:[] for x in range(1,7)}
   dict2={x:[] for x in range(1,7)}
   for i,(x,y) in enumerate(zip(A,B)):
      dict1[x].append(i)
      dict2[y].append(i)
   for x in range(1,7):
      memory=[0]*len(A) # length of given array
      for a in dict1[x]:
         memory[a]=1
      counter1=sum(memory)

      memory=[0]*len(A)
      for a in dict2[x]:
         memory[a]=1
      counter2=sum(memory)
      for a in dict1[x]:
         memory[a]=1
      if(sum(memory)==len(A)):
         return min(counter1,len(A)-counter1,counter2,len(A)-counter2)
   return -1

# recommended solution easier to understand

def find(A,B,target):
   countera=0
   counterb=0
   for i,x in enumerate(A):
      if(x==target and B[i]==target):
         continue
      if(x==target):
         countera+=1
      elif(B[i]==target):
         counterb+=1
      else:
         return -1
   return min(countera,counterb)


def solve2(var):
   # we know that if order exist it should start from first column
   A,B=var
   x=find(A,B,A[0])
   y=find(A,B,B[0])
   if(x==-1):
      return y
   elif(y==-1):
      return x
   return min(x,y)



tester=BasicTester(solve2)
tester.test(([2,1,2,4,2,2],[5,2,6,2,3,2]),2)
tester.test(([1,2,4,1,4,2,6,2],[2,3,2,2,2,2,2,2]),1)
