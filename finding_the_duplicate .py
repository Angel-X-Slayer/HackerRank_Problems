# # from array import *
# # from collections import *
# # arr=[1,2,3,4,3,5]
# # # count=1
# # c=Counter(arr)
# # print(c)
# # m=max(c.values())
# # for key,value in c.items():
# #     if(value==m):
# #         print(key)
# #         break

# ##***************************************************

# # from array import *
# # arr=[3,4,2,1,4]
# # for i in range(len(arr)):
# #     if(arr[arr[i]]<0):
# #         m=abs(arr[i])
# #         print(arr[m])
# #         break
# #     else:
# #         n=abs(arr[i])
# #         arr[n]=arr[n]*(-1)

# ##****************************************

# # from array import *
# # ar=[3,4,2,1,4]
# # p=0
# # q=0
# # m=0
# # while(True):
# #     p+=1
# #     q+=2
# #     if(ar[p]==ar[q]):
# #         m=p
# # q=0
# # print(m)
# # while(m!=q):
# #     m+=1
# #     q+=1
# # print(ar[m])


# from array import *
# ar=[3,4,2,1,3]
# t=ar[0]
# h=ar[0]
# while(True):
#     t=ar[t]
#     h=ar[ar[h]]
#     if(t==h):
#         m=t
#         break
# n=0
# while(m!=n):
#     m=ar[ar[m]]
#     n=ar[ar[n]]
# print(m)


























# # for i in range(len(arr)):
# #     for j in range(len(arr)):
# #         if(i==j):
# #             continue
# #         elif(arr[i]==arr[j]):
# #             count+=1
# #     print(count,end="\n")
# #     count=1




nums=[3,4,2,1,3]
if len(nums) <= 1:
    print -1

if len(nums) > 1:
        
    tortoise = hare = nums[0]

        
while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]

            
        if tortoise == hare:
            break

        
hare = nums[0]
while hare != tortoise:
    hare = nums[hare]
    tortoise = nums[tortoise]
        
print(hare)

    