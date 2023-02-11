# # from array import *
# # from collections import *
# # arr=[1,2,3,4,5,4,3,2,1,3,4]
# # c=Counter(arr)
# # list(c)
# # m=max(c.values())
# # for key,value in c.items():
# #     if (value==m):
# #         print(key)
# #         break

    


# # # m=max(ar)
# # # ar.sort()
# # # count=0
# # # k=3
# # # n=6   
# # # for i in range(n):
# # #     for j in range(i+1,n):
# # #         if((ar[i]+ar[j])%k==0):
# # #             count=count+1
# # # # print(count)
# # # # print(m)
# # # fruit = {
# # #     "banana": 1.00,
# # #     "apple": 1.53,
# # #     "kiwi": 2.00,
# # #     "avocado": 3.23,
# # #     "mango": 2.33,
# # #     "pineapple": 1.44,
# # #     "strawberries": 1.95,
# # #     "melon": 2.34,
# # #     "grapes": 0.98
# # # }

# # # for key,value in fruit.items():
# # #     if value == 2.00:
# # #          print(key)
# import math
# import os
# import random
# import re
# import sys
# from array import *
# from collections import *
# # Complete the migratoryBirds function below.
# def migratoryBirds(arr):
#     c=Counter(arr)
#     m=long(max(c.values()))
#     for key,value in c.items():
#         if (value==m):
#             return(key)
#             break

    
        
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# ## electronic shop code
# #  elif((L+h)<b):
# #         return(L+h)
# #     elif((l+H)<b):
# #         return(l+H)
# from array import *

# s= array [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#   ]
# print(s)


# a=[100,100,50,40,40,20,10]
# a=list(set(a))
# a.sort()
# print(a)


# word="zapa"
# alpha="a"
# number=0
# for i in range(26):
#     alpha+=1
#     print(alpha,end="\n")


##............................................##

from collections import *
a=[1,2,4,8,3,2,4,4,5,6,8,8,9,9,10,9]
d=Counter(a)
print (d)

