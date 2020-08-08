import sys
sys.path.append("..")
from BasicTester import BasicTester

def multiply(c):
   a,b=c

   minimum=a if(len(a)<len(b)) else b
   maximum=a if(len(a)>=len(b)) else b
   
   maximum=maximum[::-1]
   minimum=minimum[::-1]

   ret=0
   for i,x in enumerate(minimum):
      reminder=0
      result=0
      for ii,y in enumerate(maximum):
         reminder=reminder+int(x)*int(y)
         if(ii==len(maximum)-1):
            result+=reminder*(10**ii)*(10**i)
         else:
            result+=(reminder%10)*(10**ii)*(10**i)
            reminder=reminder//10
      ret+=result
   return ret


testme=BasicTester(multiply)
testme.test(("123","456"),123*456)
testme.test(("9999999","999999"),9999999*999999)
testme.test(("123456","123"),123456*123)

