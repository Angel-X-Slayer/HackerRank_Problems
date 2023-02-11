# n=1234
# m=0
# r=0
# while(n!=0):
#     r=n%10
#     n=int(n/10)
#     m=m*10+r
    
# print(int(m))
# d=5//2
# print(d)


# for i in range(2-1):
#     print(i)
##oporer dike sob reverse of an array er code gulo lekhar chesta kore6i


## rotating an array k places right
# k=2
# a=[1,2,3]
# queries=[0,1,2]
# for i in range(k):
#     temp=a[len(a)-1]
#     for j in range(len(a),1,-1):
#         a[j-1]=a[j-2]
#     a[0]=temp
# for i in queries:
#     print(a[i],end="\n")


## rotating an array k places right
# k=2
# a=[1,2,3]
# queries=[0,1,2]
# for i in range(k):
#     temp=a[len(a)-1]
#     for j in range(len(a),1,-1):
#         a[j-1]=a[j-2]
#     a[0]=temp
# for i in queries:
#     print(a[i])


## rotating an array k places right
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# n,k,q=map(int,input().split())
# a=[]
# queries=[]
# for i in range(n):
#     x=int(input(""))
#     a.append(x)
# for i in range(q):
#     y=int(input(""))
#     queries.append(y)
    
# circulararrayrotation(a,k,queries)



## used to rotate an array k places to the right    
# def circulararrayrotation(a,k,queries):
#     for i in range(k):
#         temp=a[len(a)-1]
#         for j in range(len(a),1,-1):
#             a[0]=temp
#             a[j-1]=a[j-2]
#         a[0]=temp
#     for w in queries:
#         print(a[w]) 


## used to rotate an array in juggling algo
# b=[]
#     for i in range(len(a)-1):
#         if((i+2)>(len(a)-1)):
#             j=(i+2)-n
#             temp=a[j]
#             a[j]=a[i]
#             a[i]=temp
#         else:
#             temp=a[i+2]
#             a[i+2]=a[i]
#             a[i]=temp
#     for w in queries:
#         x=a[w]
#         b.append(x)
#     return(b)
    
    
# for i in range(2,3):
#     print(i)
# m=9
# k=15
# c=abs(m-k)
# print(c)    
# for i in range(1,0,-1):
#     print(i)

# b=[]
# k=17
# n=10
# a=[1,2,3,4,5,6,7,8,9,0]
# o=k-n
# for i in range(o,0,-1): 
#     j=len(a)-i
#     x=a[j]
#     b.append(x)
# for i in range(0,(n-o)):
#     x=a[i]
#     b.append(x)
# print(b)

##sequence equation hackerRAnk, chutiya marka problem eta, mathar gar marie rakhe dilo
# import itertools
# numbers=[2,3,1]
# result=itertools.permutations(numbers,2)
# # for i in result:
# #     print(i)
# count=1
# while(count<=len(numbers)):
#     for i in range(result):
#         if(numbers[i[0]-1]==count):
#             for j in range(2):
#                 if(numbers[(i[j])-1]==count):
#                     k=j+1
#                     if numbers[i[k]-1]==i[j]:
#                         print(i[k])
#                         count+=1
#                         continue
    
    
class Computer:
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu
        print("Configaration is ", self.ram,self.cpu) 
com1=Computer('i5','16gb') 
com2=Computer('i7','32gb')  
    
    