# s=input("enter the string: ")
# n=len(s)
# a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# d=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# x=0
# y=0
# z=0
# w=0
# for i in range(0,n):
#     if(s[i]=="P"):
#         a[0]=a[0]+1
#         i+=1
#         if(s[i]=="0"):
#             i+=1
#             j=s[i]
#             j=int(j)
#             a[j]=1
#         else:
#             j=int([i])
#             i=i+1
#             e=int(s[i])
#             f=(j*10)+e
#             a[f]=a[f]+1
#     elif(i=="K"):
#         b[0]=b[0]+1
#         i+=1
#         if(s[i]=="0"):
#             i+=1
#             j=s[i]
#             j=int(j)
#             b[j]=1
#         else:
#             j=int(s[i])
#             i=i+1
#             e=int(s[i])
#             f=(j*10)+e
#             b[f]=b[f]+1
#     elif(i=="H"):
#         c[0]=c[0]+1
#         i+=1
#         if(s[i]=="0"):
#             i+=1
#             j=s[i]
#             j=int(j)
#             c[j]=1
#         else:
#             j=int(s[i])
#             i=i+1
#             e=int(s[i])
#             f=(j*10)+e
#             c[f]=c[f]+1
#     elif(i=="T"):
#         d[0]=d[0]+1
#         i+=1
#         if(s[i]=="0"):
#             i+=1
#             j=s[i]
#             j=int(j)
#             d[j]=1
#         else:
#             j=int(s[i])
#             i=i+1
#             e=int(s[i])
#             f=(j*10)+e
#             d[f]=d[f]+1
# for i in range(1,len(a)):
#     if(a[i]==2 or b[i]==2 or c[i]==2 or d[i]==1):
#         print("ERROR")
#         break

# for i in range(1,len(a)):
#     if(a[i]==1):
#         x=x+1
# for i in range(1,len(a)):
#     if(b[i]==1):
#         y=y+1
# for i in range(1,len(a)):
#     if(c[i]==1):
#         z=z+1
# for i in range(1,len(a)):
#     if(d[i]==1):
#         w=w+1
# # print(13-x,end=" ")
# # print(13-y,end=" ")
# # print(13-z,end=" ")
# # print(13-w,end=" ")
# print(a)
# print(b)
# print(c)
# print(d)


s=input("Enter the string: ")
n=len(s)
a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
d=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
w=0
x=0
y=0
z=0
for i in range(0,n,3):
    if(s[i]=="P"):
        i+=1
        j=int(s[i])
        i+=1
        l=int(s[i])
        m=(j*10)+l
        a[m]+=1
    elif(s[i]=="K"):
        i+=1
        j=int(s[i])
        i+=1
        l=int(s[i])
        m=(j*10)+l
        b[m]+=1
    elif(s[i]=="H"):
        i+=1
        j=int(s[i])
        i+=1
        l=int(s[i])
        m=(j*10)+l
        c[m]+=1
    elif(s[i]=="T"):
        i+=1
        j=int(s[i])
        i+=1
        l=int(s[i])
        m=(j*10)+l
        d[m]+=1
if(max(a)>1 or max(b)>1 or max(c)>1 or max(d)>1):
    print("ERROR")
else:
    print((13-sum(a)),end=" ")
    print((13-sum(b)),end=" ")
    print((13-sum(c)),end=" ")
    print((13-sum(d)),end=" ")

# print(a)
# print(b)
# print(c)
# print(d)     

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        