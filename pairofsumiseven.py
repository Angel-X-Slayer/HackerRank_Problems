from array import *
arr=array('i',[])
t=int(input("enter the number of test cases :"))
for i in range(t):
    x=int(input("Enter the 1st limit :"))
    y=int(input("enter the 2nd limit :"))
    c=0
    for i in range(1,x+1):
        for j in range(1,y+1):
            if((i+j)%2==0):
                c=c+1
    arr.append(c)
for i in arr:
    print(i,end="\n")
    
