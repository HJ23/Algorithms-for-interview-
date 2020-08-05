import sys
sys.path.append("..")
from BasicTester import BasicTester

def find(C):
   A,B=C

   if(len(A)!=len(B)):
      return False
   if(A==B and len(set(A))!=len(A)):
      return True
   found=False
   index=-1
   A=list(A)
   B=list(B)
   for i,x in enumerate(A):
      if(B[i]!=x and not found):
         found=True
         index=i
      elif(B[i]!=x and found):
         tmp=A[index]
         A[index]=x
         A[i]=tmp
         if("".join(A)== "".join(B)):
            return True
         else:
            return False
   return False


testme=BasicTester(find)
testme.test(("ab","ba"),True)
testme.test(("abc","abd"),False)
testme.test(("","aaa"),False)
testme.test(("abab","abab"),True)
testme.test(("aaa","aaa"),True)




