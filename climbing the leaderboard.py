from array import *
from collections import *
result=[]
ranked=[100,100,50,40,40,20,10]
player=[5,25,50,120]
# l=len(ranked)
# for i in player:
#     for j in range(l-1,-1,-1):
#         if(i<ranked[j]):
#             ranked.insert(j+1,i)
            # c=Counter(ranked)
            # for key,value in c.items():
            #     if (value==i):
            #         print(value)
            #         break
ranked=sorted(list(set(ranked)),reverse=True)
player.sort(reverse=True)
l=len(ranked)
print(ranked)
print(player)
print(l)



