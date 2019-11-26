# Complexity O(n^2)


tri1=[[2],[3,4],[6,5,7],[4,1,8,3]]

def triangle(array):
    sums=[]
    for layer in range(len(array)-2,-1,-1):
        sums=[]
        for index in range(len(array[layer])-1,-1,-1):
            sums.insert(0,min(array[layer+1][index],array[layer+1][index+1])+array[layer][index])
        array[layer]=sums

    return sums


print(triangle(tri1))
                
            
                    
        














