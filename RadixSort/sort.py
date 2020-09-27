from count import counting_sort

def radix(arr=[12,34,657,12,0,1,2,444]):
   maxi=len(str(max(arr,key=lambda x:len(str(x)))))
   for x in range(maxi):
      tmp=[]
      keys={0:[]}
      for element in arr:
         if(len(str(element))-1<x):
            keys[0].append(element)
            tmp.append(0)
         elif(int(str(element)[x]) in keys):
            keys[int(str(element)[x])].append(element)
            tmp.append(int(str(element)[x]))
         else:
            keys[int(str(element)[x])]=[element]
            tmp.append(int(str(element)[x]))
      ret=counting_sort(tmp)
      a=[]
      for x in ret:
         a.append(keys[x].pop(0))
      arr=a

   return arr

print(radix())
