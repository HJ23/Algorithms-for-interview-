def happy(num):
   memory=set()
   sumsquare=lambda x:sum(map(lambda x:int(x)**2,list(str(x)) ))
   while(not num in memory):
      memory.add(num)
      num=sumsquare(num)
      if(num==1):
         return True
   return False
