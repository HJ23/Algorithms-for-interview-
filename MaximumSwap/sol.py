
def find(num):
   numl=[int(x) for x in str(num)]
   dict={x:[] for x in range(0,10)}
   for i,x in enumerate(numl):
      dict[x].append(i)

   ret=list(numl)

   for x in range(9,-1,-1):
      for i,y in enumerate(numl):
         if(len(dict[x])!=0 and x>y and dict[x][-1]>i):
            tmp=dict[x].pop(-1)
            ret[tmp]=ret[i]
            ret[i]=x
            return "".join([str(x) for x in ret])
   return num
