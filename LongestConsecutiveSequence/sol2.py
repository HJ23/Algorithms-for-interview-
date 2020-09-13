def find(arr):
   set_=set(arr)
   maxi=0
   while(set_):
      f=l=set_.pop()
      while(f-1 in set_):
         f-=1
         set_.remove(f)
      while(l+1 in set_):
         l+=1
         set_.remove(l)
      maxi=max(maxi,l-f+1)
   return maxi
