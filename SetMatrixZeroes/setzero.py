def set(matrix):
   r,c=len(matrix),len(matrix[0])
   row=[False for _ in range(r)]
   column=[False for _ in range(c)]


   for x in range(r):
      for y in range(c):
         if(matrix[x][y]==0):
            row[x]=True
            column[y]=True
   for x in range(r):
      for y in range(c):
         if(row[x] or column[y]):
            matrix[x][y]=0

mat=[[1,2,0],
     [2,9,1],
     [0,1,2]]

set(mat)

print(mat==[[0,0,0],[0,9,0],[0,0,0]])


