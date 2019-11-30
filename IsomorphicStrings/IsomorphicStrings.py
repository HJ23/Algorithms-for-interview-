# Isomorphic String check
# Complexity O(n) -> amortized

def iso(str1,str2):
   dict={}
   if(len(str1)!=len(str2)):
      return False
   else:
      for x in range(len(str1)):
          if(not str1[x] in dict):
              dict[str1[x]]=str2[x]
          if(dict[str1[x]]!=str2[x] or str2[x] in dict):
               return False
      return True

str1="abaabek"
str2="cdccdke"

print(iso(str1,str2) )
