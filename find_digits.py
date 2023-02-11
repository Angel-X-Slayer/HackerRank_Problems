n=1201
a=[]
dig=0
t=n
while(n!=0):
    r=int(n%10)
    n=int(n/10)
    a.append(r)
for i in a:
    if(i==0):
        pass
    else:
        if(t%i==0):
            dig+=1
print(dig)
# print(a)