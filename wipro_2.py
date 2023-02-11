# D=int(input("enter the days: "))
# d=int(input("enter the time interval: "))
# p=int(input("enter the initial rate: "))
# q=int(input("enter the increased rate: "))
test=int(input(""))
out_arr=[]
for i in range(test):
    # inarr=list(map(int,input().split(" ")))
    # D=inarr[0]
    # d=inarr[1]
    # p=inarr[2]
    # q=inarr[3]
    D,d,p,q=map(int,input().split(" "))
    k=int(D/d)
    tot=0
    m=0
    for i in range(k+1):
        if m<D and D-m>d:

            sum=d*(p+(i*q))
            tot+=sum
            m+=d
        else:
            sum=(D-m)*(p+(i*q))
            tot+=sum

    # print(tot)
    out_arr.append(tot)
for i in out_arr:
    print(i,end="\n")