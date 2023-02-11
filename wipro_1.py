# n=int(input("enter the number:"))
# sum=17
# # for i in range(3,n):
# #     if i%2!=0:
# #         sum+=i
# #     if sum>n:
# #         sum-=1
# #     else:
# #         pass
# i=8
# a=[]
# a.append(2)
# a.append(3)
# a.append(5)
# a.append(7)
# while sum<n:
#     if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#         sum+=i
#         a.append(i)
#     i+=1
# if sum>n:
#     a.pop(len(a)-1)
# print(a)
def find_prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k+=1
    if k==0:
        return 1
    else:
        return 0
def solution(n):
    a=[]
    a.append(2)
    sum=2
    for i in range(3,n):
        m=find_prime(i)
        if m==1:
            sum+=i
            a.append(i)
        if sum>n:
            print("not summable...")
            break
        elif sum==n:
            print(a)
            print("summable...")
            break
        else:
            continue  
q=int(input("enter the number : "))
solution(q)