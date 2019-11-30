# Complexity O(nlog(n))

def run(array,k):
    if(k<=len(array) and k>0):
        arrayx=array.copy()
        arrayx=arrayx.sort()
        print(array[len(array)-k])

run([1,2,3,4,5],5)

