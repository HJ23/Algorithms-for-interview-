import math

def order(num):
   if(num==1):
      return True

   power=int(math.log(num,2))-1
   tmp=2**power
   func=lambda x:sorted(list(str(num)),key=lambda x:int(x),reverse=True)
   num=func(num)
   if(num==func(tmp)):
      return True
   for x in range(power,power*20):
      tmp=tmp*2
      if(num==fun(tmp)):
         return True
      if(len(num)<len(str(tmp))):
         break
   for x in range(power,power//20,-1):
      tmp=tmp//2
      if(num==fun(tmp)):
         return True
      if(len(num)>len(str(tmp))):
         break
   return False
