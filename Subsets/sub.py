def subset(arr):
   ret=[]
   length=len(arr)
   queue=[([],0)]
   while(len(queue)!=0):
      sset,index=queue.pop(0)
      if(index>length):
         continue
      ret.append(sset)
      for i,x in enumerate(arr[index:]):
         tmp=sset.copy()
         tmp.append(x)
         queue.append((tmp,index+i+1))
   return ret

