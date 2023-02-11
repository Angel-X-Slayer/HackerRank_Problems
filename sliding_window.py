inarr=list(map(int,input("enter the values in the array :").split(',')))
n=len(inarr)
k=int(input("enter the value of target :"))
cur_sum=0
max_sum=0
for i in range(n-k+1):
    cur_sum=sum(inarr[i:i+k])
    if cur_sum>max_sum:
        max_sum=cur_sum
    else:
        pass
print(max_sum)