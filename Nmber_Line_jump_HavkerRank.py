import numpy
from array import *
x1=int(input("Enter the starting point of the 1st kangaroo :"))
v1=int(input("Enter the umit line jump of the 1st kangaroo :"))
x2=int(input("Enter the starting point of the 2nd kangaroo :"))
v2=int(input("Enter the umit line jump of the 2nd kangaroo :"))

arr=array('i',[])
brr=array('i',[])
for i in range(1,100):
    x=x1+v1
    arr.append(x)
for i in range(1,100):
    y=x2+v2
    brr.append(y)
    
crr=numpy.in1d(arr,brr)
for i in crr:
    if(i=="True"):
        c="YES"
        break
    else:
        c="NO"
print(c)
