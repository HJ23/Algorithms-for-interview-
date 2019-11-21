# Isomorphic String check
# Complexity O(n) -> amortized



import os

def iso(str1,str2):
   dict={}
   if(len(str1)!=len(str2)):
      return False
   else:
      for x in range(len(str1)):
         try:
            if(dict[str1[x]]!=str2[x]):
               return False
         except:
            dict[str1[x]]=str2[x]
   return True

str1="abaab"
str2="cdcce"
print(iso(str1,str2) and iso(str2,str1))
