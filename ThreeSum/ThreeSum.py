# Complexity O(n^2)

array=[2,3,7,8,9,12,13,34,35,45,67]
target=66
def threeSum(array,target):
    
    for num3 in array:
        i=0
        j=len(array)-1
        while(j>i):
                if(num3+array[i]+array[j]>target):
                    j-=1
                elif(num3+array[i]+array[j]<target):
                    i+=1
                else:
                    if(i!=j and num3!=array[i]):
                        print(str(array[i])+" "+str(array[j])+" "+str(num3))
                        break
    
threeSum(array,target)
