def summary(arr):
   purify=lambda x:str(x[0])+"->"+str(x[1]) if(x[0]!=x[1]) else str(x[0])
   ss=set(arr)
   ret=[]
   i=0
   tmp=[]
   while(i!=len(arr)):
      for j in range(len(arr)+1):
         if(arr[i]+j in ss):
            if(len(tmp)==0):
               tmp.append(arr[i])
         else:
            break
      tmp.append(arr[i]+j-1)
      ret.append(purify(tmp))
      tmp=[]
      i+=j
   return ret

print(summary([1,2,3,5,6,7,8,122]))
