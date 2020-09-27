
def counting_sort(arr):
   nums=[0]*10
   ret=[0]*len(arr)
   for element in arr:
      nums[element]+=1
   nums=nums[0:-1]
   nums.insert(0,0)
   for x in range(1,len(nums)):
      nums[x]+=nums[x-1]
   for element in arr:
      start=nums[element]
      ret[start]=element
      nums[element]+=1
   return ret

