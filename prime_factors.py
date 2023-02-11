n=39
for i in range(2,n):
    if n%i==0:
        c=2
        for j in range(2,i):
            if i%j!=0:
                c+=1
        if c==i:
            print(i)
    else:
        pass