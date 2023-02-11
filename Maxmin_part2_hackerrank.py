from array import *
n=int(input("enter the lenth :"))
arr=array('d',[])
brr=array('d',[])
s=0
for i in range(n):
    x=int(input("Enter the value :"))
    arr.append(x)
for i in range(n):
    for j in range(n):
        if(i==j):
            continue
        else:
            s=s+arr[j]
    brr.append(s)
    s=0
print(brr)
print(max(brr))
print(min(brr))
