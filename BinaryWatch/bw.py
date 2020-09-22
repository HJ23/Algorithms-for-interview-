
def bw(num):
   ret=[]
   queue=[(0,0,0)]
   if(num>8):
      return []
   while(len(queue)!=0):
      node,count,k=queue.pop(0)
      if(count==num):
         hour=(node&0b1111000000)>>6
         minute=(node&0b0000111111)
         minute=str(minute) if(len(str(minute))==2) else "0"+str(minute)
         ret.append(str(hour)+":"+minute)
         continue
      for x in range(k,10):
         tmp=(node|1<<x)
         if(node&1<<x==0 and (tmp&0b1111000000)>>6<=11 and (tmp&0b0000111111)<=59):
            queue.append((tmp,count+1,k+1))
   return set(ret)

