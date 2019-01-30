# You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .





#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count=0
    print(arr)
    left={}
    right={}
    for a in arr:
        right[a]=right.get(a,0)+1
    for a in arr:
        print('left',left,'right',right)
        right[a]-=1
        if(left.get(a/r,0)>0 and right.get(a*r,0)>0):
            count=count+left.get(a/r,0)*right.get(a*r,0)
        left[a]=left.get(a,0)+1
    print(count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
