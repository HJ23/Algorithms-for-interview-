# Complexity is O(N^2)

array=[[1,2,3,4,9],[6,7,8,9,7],[1,2,3,4,3],[5,6,7,8,5]]

# 1,2,3,4,9
# 6,7,8,9,7
# 1,2,3,4,3
# 5,6,7,8,5

#1,2,3,4,9,7,3,5,8,7,6,5,1,6,7,8,9,4,3,2


def spiral(array):
    row=len(array)
    column=len(array[0])
    
    for x in range(0,row//2):
        for y in range(x,column-x-1):
            print(array[x][y])
            
        for p in range(x,row-x-1):
            print(array[p][column-1-x])
            
        for q in range(column-1-x,x,-1):
            print(array[row-1-x][q])
            
        for u in range(row-1-x,x,-1):
            print(array[u][x])

spiral(array)




