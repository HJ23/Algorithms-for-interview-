import time
array1=[1,2]
array2=[4,6,7,8,11,14,15]


# Method 2
# Complexity O(n+m) memory complexity O(1)

def find_MethodTwo(array1,array2):
    index_first=len(array1)-1
    index_second=len(array2)-1
    max_lenght=int(len(array1)+len(array2))
    middleIsEven=False
    if(max_lenght%2==0):
        middleIsEven=True
    else:
        middleIsEven=False
    middle=max_lenght>>1
        
    result=None
    next_element=None
    while(True):
        if(array1[index_first]>array2[index_second]):
            middle-=1
            index_first-=1
        else:
            middle-=1
            index_second-=1
        if(middle==1):
            if(array1[index_first]>array2[index_second]):
                next_element=array1[index_first]
            else:
                next_element=array2[index_second]
            
        if(middle==0):
            result=array1[index_first] if array1[index_first]>array2[index_second] else array2[index_second]
            if(middleIsEven):
                result+=next_element
                result/=2
            break
    return result
# Method one
# Complexity O(m+n)  memory Complexity O(m+n)

def find_MethodOne(array1,array2):
    temp_array=[]
    index_first=0
    index_second=0
    while(index_first!=len(array1)  and index_second!=len(array2) ):
        if(array1[index_first]<array2[index_second]):
            temp_array.append(array1[index_first])
            index_first+=1
        else:
            temp_array.append(array2[index_second])
            index_second+=1
    while(index_first!=len(array1)):
        temp_array.append(array1[index_first])
        index_first+=1
    while(index_second!=len(array2)):
        temp_array.append(array2[index_second])
        index_second+=1
    result=-1
    if(len(temp_array)%2==0):
        result=(temp_array[int((len(temp_array)-1)/2)]+temp_array[int((len(temp_array))/2)])/2 
    else:
        result=temp_array[int((len(temp_array)-1)/2)]
    return result       



if (__name__=="__main__"):
    start=time.time()
    print(find_MethodTwo(array1,array2))
    print("time elapsed for second method : "+str((time.time()-start)))
    print(find_MethodOne(array1,array2))
    print("time elapsed for first method : "+str((time.time()-start)))
