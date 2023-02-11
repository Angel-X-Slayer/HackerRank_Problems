ip=input("enter the string : ")
k=len(ip)
a=[]
def swap(a):
    o=len(a)
    i=0
    j=o-1
    while i<j:
        if i==j:
            break
        else:

            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            i+=1
            j-=1
    return (a)
for i in range(k):
    if ord(ip[i])==47 or ord(ip[i])==92:
        temp=i
        for j in range(temp+1,k):
            if ord(ip[j])==47 or ord(ip[j])==92:
                temp1=j
                a.append(ip[temp+1:temp1])
                break
t=swap(a)

print(*t,sep=" ")

