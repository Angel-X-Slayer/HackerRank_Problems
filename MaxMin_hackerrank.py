from array import *
arr=array('i',[])
n=int(input("enter the lenth of the array :"))
for i in range(n):
    x=int(input(f"enter the {i+1} element of the array :"))
    arr.append(x)
minsum=0
maxsum=0
lenth=len(arr)
    
for i in range (4):
    minsum=minsum+arr[i]
    for i in range(4):
        maxsum=maxsum+arr[lenth-i-1]
print(f"minimum sum is {minsum}")       
print(f"maximum sum is {maxsum}")  
