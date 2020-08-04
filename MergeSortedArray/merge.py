import sys
sys.path.append("..")


def merge(nums1, m: int, nums2, n: int) -> None:
   i=0
   j=0
   tmp=[]
   while(i!=m and j!=n):
      if(nums1[i]>nums2[j]):
         tmp.append(nums2[j])
         j+=1
      else:
         tmp.append(nums1[i])
         i+=1

   while(i!=m):
      tmp.append(nums1[i])
      i+=1
   while(j!=n):
      tmp.append(nums2[j])
      j+=1

   for i,x in enumerate(tmp):
      nums1[i]=x


a=[1,2,3,0,0,0,0]
b=[1,2,5,6]
merge(a,3,b,4)
print(a==[1,1,2,2,3,5,6])
