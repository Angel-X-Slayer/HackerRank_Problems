# n=10
# b=2
# k=int(n/b)
# a=[]
# for i in range(k,0,-1):
#     b1=n-(b*i)
#     if b1==0:
#         a.append(0)
#     else:
#         m=int(b1/1)
#         p=(m*1)*i
#         a.append(p)
# o=max(a)

# print(a)
# print(o)





# a=[10,41,18,50,43,31,29,25,59,96,67]
# sum=0
# c=[]
# for i in range(len(a)):
#     flag=0
#     for j in range(2,a[i]):
#         if a[i]%j==0:
#             flag=1
#             break
#     if flag==0:
#         c.append(a[i])
# c.sort()
# for i in range(1,len(c)):
#     sum+=c[i]
# print(sum)




# print("hello world(print("hello world("hello world")")")
# i=10
# k=(bin(i).replace("0b",""))
# arr=[]
# arr[i]=k
# print(arr)




def binaryofnum(i):
    return(bin(i).replace("0b",""))
def onesinbin(j):
    one_count=0
    j=str(j)
    for i in j:
        if i=="1":
            one_count+=1
    return(one_count)          
def cardinalitySort(nums):
    arr=[]*100
    brr=[]*100
    for i in range(len(nums)):
        k= binaryofnum(nums[i])
        # arr[nums[i]]=k
        arr.insert(nums[i],k)
    for i in range(len(arr)):
        l=onesinbin(arr[i])
        # brr[nums[i]]=l
        brr.insert(nums[i],l)
    zipped_pairs = zip(brr, nums)
 
    z = [x for _, x in sorted(zipped_pairs)]
     
    print(arr)
    print(brr)
    print(z)

# nums=[1,2,3,4]
nums=[5,31,15,7,3,2]
# p=sorted(nums)
print(nums)
cardinalitySort(nums)































# def findless(teamA,k):
#     l=len(teamA)
#     c=0
#     # for i in teamA:
#     #     if i<=k:
#     #         c+=1
#     #     else:
#     #         pass
#     i=0
#     while i>l:
#         if (teamA[i]<=k):
#             c+=1
#             i+=1
#         else:
#             break
#     l1=l-c
#     return(l1)
# def counts(teamA, teamB):
#     # Write your code here
#     arr=[]
#     teamA=sorted(teamA)
#     teamb=sorted(teamB)
#     for i in range(len(teamB)):
#         k=teamB[i]
#         y=findless(teamA,k)
#         arr.append(y)
#     print(arr)
# a=[1,4,2,4]
# b=[3,5]
# counts(a,b)