def reshape(var):
   matrix,r,c=var
   if(r*c!=len(matrix)*len(matrix[0])):
      return matrix
   cc=0
   ret=[]
   tmp=[]
   for x in range(len(matrix)):
      for y in range(len(matrix[0])):
         if(cc%c==0 and cc!=0):
            cc=0
            ret.append(tmp)
            tmp=[]
         tmp.append(matrix[x][y])
         cc+=1
   ret.append(tmp)
   return ret

print(reshape(([[1,2,3,4],[4,5,6,8]],4,2)))
