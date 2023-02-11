from array import *
arr=array('i',[])
brr=array('i',[])
n=int(input())
for i in range(n):
    x=int(input())
    if(x>=38):
        rem=x%5
        divminus=5-rem
        if(divminus<3):
            x=x+divminus
        else:
            x=x+0
    else:
        x=x+0
    brr.append(x)
print()
for i in brr:
    print(i,end="\n")
    