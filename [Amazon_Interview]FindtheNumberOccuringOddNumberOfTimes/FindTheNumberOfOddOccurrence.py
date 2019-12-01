def find(array):
   temp=array[0]
   for index in range(1,len(array)):
      temp=temp^array[index]
   return temp

print(find([1,1,2,3,22,22,3,3,2]))
