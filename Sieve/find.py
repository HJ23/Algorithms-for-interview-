import math

def prime(n):
   tmp=[False for _ in range(0,n+1)]
   ret=[]
   for x in range(2,n+1):
      found=False
      if(tmp[x]):
         continue
      for y in range(1,int(math.sqrt(x))+1):
         if(x%y==0 and y!=1):
            found=True
            break
      if(not found):
         ret.append(x)
      for p in range(2,n//x):
         tmp[p*x]=True
   return ret

print(len(prime(10000)))
