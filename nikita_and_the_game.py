import os
from numpy import *
from array import *
arr=array('i',[])
n=int(input("enter the lenth of the array :"))
for i in range(n):
    x=int(input("enter the value :"))
    arr.append(x)
arr.Sorting()
print(arr)


