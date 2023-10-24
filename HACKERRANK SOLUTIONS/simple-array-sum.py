import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

n = int(input())
nums = list(map(int, input().split()))
sum = 0
for num in nums:
    sum += num
print(sum)
