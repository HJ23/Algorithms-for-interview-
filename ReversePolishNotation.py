#   Reverse Polish Notation
#   Complexity O(n)
#

import os
from collections import deque

def operationCheck(operation, item1, item2):
    result = 0
    if (operation == "+"):
        result = item1 + item2
    elif (operation == "-"):
        result = item2 - item1
    elif (operation == "*"):
        result = item1 * item2
    elif (operation == "/"):
        result = int(item2 / item1)
    return result


if (__name__ == "__main__"):
    array = ["4", "15", "5", "/", "+"]
    stack = deque()
    result = 0
    for arrayItem in array:
        if (arrayItem != '+' and arrayItem != "*" and arrayItem != "-" and arrayItem != "/"):
            stack.append(arrayItem)
        else:
            if (len(stack) == 1):
                result = operationCheck(arrayItem, int(stack.pop()), result)
            else:
                result = operationCheck(arrayItem, int(stack.pop()), int(stack.pop()))
    print(result)
