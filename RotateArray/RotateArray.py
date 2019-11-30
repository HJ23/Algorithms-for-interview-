#    Rotate array without using any auxiliary array or data structure
#    by k step
#    Complexity O(n) for with Auxiliary array solution     memory complexity O(n)
#    Complexity O(n*k) for without memory (k is step size) memory complexity O(1)

import time

def rotateAux(step, array):
    arrayAux = []
    start = time.time()
    for x in range(0, (len(array) - step)):
        arrayAux.append(array[x])
    for x in range(len(array) - 1, len(array) - step - 1, -1):
        arrayAux.insert(0, array[x])
    delay = (time.time() - start)
    print("array : {}  , delay : {}".format(arrayAux, delay))


def rotate(step, array):
    start = time.time()
    for k in range(step):
        item1 = array[len(array) - 1]
        for x in range(0, len(array)):
            item2 = array[x]
            array[x] = item1
            item1 = item2
    delay = (time.time() - start)
    print("array : {}  , delay : {}".format(array, delay))


if(__name__=="__main__"):
    rotate(3, [1, 2, 3, 4, 5, 6, 7])
    rotateAux(3, [1, 2, 3, 4, 5, 6, 7])
