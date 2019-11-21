#   Reverse Words in a String
#   Complexity O(n)

import os
from collections import deque

stack = deque()
temp = ""
sentence = "Today weather is warm. Anna went to school with her friend."
array = sentence.split(" ")

for item in array:
    stack.append(item)

while (stack.__len__() != 0):
    temp += stack.pop() + " "
print(temp)
