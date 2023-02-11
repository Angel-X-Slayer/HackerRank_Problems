import math
import os
import random
import re
import sys
from array import *

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s=0
    brr=array('i',[])
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if(i==j):
                continue
            else:
                s=s+arr[j]
    brr.append(s)
    s=0
    print(max(brr),end=" ")
    print(min(brr))

        
    
    
                
    
                  
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)