# Complexity O(max(m,n)) -> m,n are lenght of given strings

def sumBinary(a,b):
   reminder=0
   mini=a if(len(a)<len(b)) else b
   maxi=a if(len(a)>=len(b)) else b
   mini=mini[::-1]
   maxi=maxi[::-1]
   ret=""
   for i,x in enumerate(mini):
      tmp=reminder+int(x)+int(maxi[i])
      ret=ret+str(tmp%2)
      reminder=tmp//2
   if(reminder==0):
      return (ret+maxi[len(mini):])[::-1]
   for x in range(len(mini),len(maxi)):
      tmp=reminder+int(maxi[x])
      ret=ret+str(tmp%2)
      reminder=tmp//2
   if(reminder!=0):
      return (ret+"1")[::-1]
   return ret[::-1]

#Tests
assert sumBinary("11","11")=="110"
assert sumBinary("1","11")=="100"
assert sumBinary("111","111")=="1110"
assert sumBinary("101","1")=="110"
assert sumBinary("101","101")=="1010"
assert sumBinary("11","00")=="11"
