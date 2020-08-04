import math

# solution 1
def calculate_binarysearch(num):
   l=0
   r=num//2
   while(l<=r):
      midd=(l+r)//2
      if(midd*midd>num):
         r=midd-1
      elif(midd*midd<num):
         l=midd+1
      else:
         return midd
   return l-1

# solution 2

def calculate_Newton_Raphson(num):
   N=num
   pre=num+1
   threshold=0.1
   while(abs(pre-num)>threshold):
      pre=num
      num=0.5*(num+N/num)
   return math.floor(num)


def get(num,method="bs"):
   if(num==0 or num==1):
      return num
   if(method=="bs"):
      return calculate_binarysearch(num)
   elif(method=="nr"):
      return calculate_Newton_Raphson(num)
   else: 
      return -1


print(get(1000,"nr"))
