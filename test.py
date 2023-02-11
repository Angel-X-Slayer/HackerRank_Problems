# import math

# from matplotlib.cbook import pts_to_midstep
# arr=[]
# n=int(input())
# for i in range(n):
#     num=int(input())
#     arr.append(num)
# print(arr)
# a,b,c=map(int,input().split())
# print(a,b,c,a+b+c)
# bar = [EXPRESSION for item in some_iterable]
# print(bar)
# a=
# # print(a)
# bar = []
# for item in some_iterable:
#     bar.append(SOME EXPRESSION)
# d=[x[:] for x in [[for * 10] * 10]  
# print(d)

# n=3
# magicSquare = [[0 for x in range(n)]
# 				for y in range(n)]
# print(magicSquare)
# n=10
# magic=[[[]for x in range(n)]for y in range(n)]

# for i in range(n):
# 	for j in range(n):
# 		magic[i][j]="A"
		
# for i in range(n):
# 	for j in range(n):
# 		print(magic[i][j],end=" ")
# 	print()

# print(magic)
# magic1=[[]]
# print(magic1)
# n=9
# maxFromEnd = [-38749432] * (n + 1)
# print(maxFromEnd)



# a = [34, 8, 10, 3,3, 2, 80, 30, 33, 1]
# n=10
# # To store the index of an element.
# index = dict() 
# for i in range(n):
#     if a[i] in index:

#         # append to list (for duplicates)
#         index[a[i]].append(i)  
#     else:

#         # if first occurrence
#         index[a[i]] = [i]   
# print(index)






## ArraY_BM_41,my version
# def max_idx(arr):
#     i=0
#     brr=[]
#     j=i+1
#     while i<len(arr):
#         if arr[i]<=arr[j]:
#         # if arr[i]<=arr[j]:
#             # d=j-i
#             # brr.append(d)
#             # i+=1
#             d=j=i
#             brr.append(d)
#             j+=1
#         else:
#             # d=j-i
#             # i+=1
#             # j=i+1
#             # brr.append(d)
#             i+=1
#             j=i+1
#     print(max(brr))

# # arr=[34,8,10,3,2,80,30,33,1]
# arr=[9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
# max_idx(arr)


# def binarysearch(key,arr,l,r):
#     if l<=r:
#         mid=(l+r)//2
#         if arr[mid]==key:
#         #return arr[mid], # this return statement is for this programme
#             return(1)

#         if arr[mid]<key:
#             return(binarysearch(key,arr,mid+1,r))
#         #elif arr[mid]>key:
#         else:
#             return(binarysearch(key,arr,l,mid-1))
#     else:
#         return(-1)
# arr=[1,2,3]#,4,5,6,7,8]]
# key=3
# print(binarysearch(key,arr,0,(len(arr)-1)))

# w,n=7,4
# t=[[-1 for i in range(4)]for j in range(7)]
# ## t=[[-1 for i in range(column) for j in range(row)]]
# for k in range(7):
#     for m in range(4):
#         print(t[k][m],end=" ")
#     print()
##for k in range(row):
##  for m in range(column):
##      print(t[row][column],end=" ")
##  print()
# t=0

# for i in range(7):
#     for j in range(4):
#         t[i][j]=2
# print(t)

# x='pythonprog'
# print(x.isalpha())









# def tower_of_hanoi(n,source,destination,intermidiate):
#     if n>=1:
#         tower_of_hanoi(n-1,source,destination,intermidiate)
#         print(f"Move { source } -> { destination } ")
#         tower_of_hanoi(n-1,source,intermidiate,destination)


# n,source,destination,intermidiate=3,1,3,2
# tower_of_hanoi(n,source,destination,intermidiate)
# Recursive Python function to solve the tower of hanoi

# Dynamic Programming Python implementation of Coin
# 
# Change proble
# m
# def remove(string):
#     return string.replace(" ", "")
      
# Driver Program
# def remove(string):
#     return "".join(string.split())
      
# # Driver Program
# string = ' A man, a plan, a canal: Panama '
# print(remove(string))



# a=[12,221,34567,47,51,60]
# # produ=numpy.prod(a[0:0+3])
# # print(produ)
# for i in range(len(a)-2,int(len(a)/2)-1,-1):
#     print(a[i],end=" ")



# def freqn(arr):
#     freq={}
#     for i in arr:
#         if i not in freq.keys():
#             freq[i]=1
#         else:
#             freq[i]+=1
#     for i in freq.keys():
#         print(f"{i} {freq[i]}")
# if __name__=="__main__":
#     arr=list(map,int(input("enter the values : "),split(",")))
#     freqn(arr)

# arr=list(map(int,input("enter the values :").split(",")))
# print(arr)
# a = 5
#this will print a in binary
# bnr = bin(a).replace('0b','')
# x = bnr[::-1] #this reverses an array
# while len(x) < 7:
#     x += '0'
# bnr = x[::-1]
# print(bnr)
# a = "11011111101100110110011001011101000"
# b = "11001011101100111000011100001100001"
# y = int(a,2) ^ int(b,2)
# print (f'{0:b}'.format(y))
# a = "1000"
# b = "110"
# y = int(a, 2)^int(b,2)
# print (bin(y)[2:].zfill(len(a)))

# bnr = bin(7).replace('0b','')
# print(bnr)
# nb=0b0111
# nb=bin(nb)
# if bnr==nb:
#     print(bnr)
# Python3 code to demonstrate
# yield keyword

# generator to print even numbers
# def print_even(test_list) :
# 	for i in test_list:
# 		if i % 2 == 0:
# 			yield i

# # initializing list
# test_list = [1, 4, 5, 6, 7]

# # printing initial list
# print ("The original list is : " + str(test_list))

# # printing even numbers
# print ("The even numbers in list are : ", end = " ")
# for j in print_even(test_list):
# 	print (j, end = " ")
# Python program to print level
# order traversal using Queue

# A node structure


# class Node:
# 	# A utility function to create a new node
# 	def __init__(self, key):
# 		self.data = key
# 		self.left = None
# 		self.right = None

# # Iterative Method to print the
# # height of a binary tree


# def printLevelOrder(root):
# 	# Base Case
# 	if root is None:
# 		return

# 	# Create an empty queue
# 	# for level order traversal
# 	queue = []

# 	# Enqueue Root and initialize height
# 	queue.append(root)

# 	while(len(queue) > 0):

# 		# Print front of queue and
# 		# remove it from queue
# 		print(queue[0].data)
# 		node = queue.pop(0)

# 		# Enqueue left child
# 		if node.left is not None:
# 			queue.append(node.left)

# 		# Enqueue right child
# 		if node.right is not None:
# 			queue.append(node.right)


# # Driver Program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# print("Level Order Traversal of binary tree is -")
# printLevelOrder(root)
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# Python program to do inorder traversal without recursion

# # A binary tree node
# class Node:
	
# 	# Constructor to create a new node
# 	def __init__(self, data):
# 		self.data = data
# 		self.left = None
# 		self.right = None

# # Iterative function for inorder tree traversal
# 	def inorder(self, data):
# 		c=Node(data)
	
# 	# Set current to root of binary tree
# 		current = c
# 		stack = [] # initialize stack
	
# 		while True:
		
# 		# Reach the left most Node of the current Node
# 			if current is not None:
			
# 			# Place pointer to a tree node on the stack
# 			# before traversing the node's left subtree
# 				stack.append(current)
		
# 				current = current.left

		
# 		# BackTrack from the empty subtree and visit the Node
# 		# at the top of the stack; however, if the stack is
# 		# empty you are done
# 			elif(stack):
# 				current = stack.pop()
# 				print(current.data, end=" ") # Python 3 printing
		
# 			# We have visited the node and its left
# 			# subtree. Now, it's right subtree's turn
# 				current = current.right

# 			else:
# 				break
	
# 		print()

# # Driver program to test above function

# """ Constructed binary tree is
# 			1
# 		/ \
# 		2	 3
# 	/ \
# 	4 5 """

# root = Node(1)
# root.inorder(2)
# root.inorder(3)
# root.inorder(4)
# root.inorder(5)
# root.inorder(6)



# This code is contributed by Nikhil Kumar Singh(nickzuck_007)





# from json import decoder, encoder


# shift=3
# encode=[None]*26
# decode=[None]*26
# for k in range(26):
# 	encode[k]=chr((k+shift)%26+ord('A'))
# 	decode[k]=chr((ord(encode[k])-shift)%26+ord('A'))
# 	# decode[k]=chr((ord(encode[k])-shift)%26+ord('A')))
# # msg=input("enter the mesage :")
# # msg=list(msg)
# # for i in range(len(msg)):
# # 	if ord(msg[i])>=97:
# # 		msg[i]=chr(ord(msg[i])-32)
# # 	else:
# # 		pass
# # print(msg)

# # code=[]
# # for i in range(len(msg)):
# # 	if msg[i].isupper():
# # 		code[i]=chr(ord(msg[i])+(shift%26))

# print('  '.join(encode))
# print('  '.join(decode))
# print(''.join(msg))
# print(''.join(code))


# a=chr(88)
# print(a)
# b=(3)%26
# print(b)


# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# c=a+b
# print("the sum is:",c)




# for i in range(10,0,-1):
#     print(i)

# tot=[1,1,1,0,0,1,1,0,0,1,0,0]
# r=4
# m=8
# sum=[]
# r0=[]
# sol=[]
# for i in range (r):
#     k=pow(2,i)
#     i1=0
#     l=k
#     while l<r+m:
#         if i1<k:
#             r0.append(l)
#             i1+=1
#             l+=1
#         elif i1==k:
#             for i1 in range(k-1,-1,-1):
#                 l+=1
#     for q in r0:
#         sum+=tot[q]
#         if q%2==0:
#             sol.append(0)
#         else:
#             sol.append(1)
    
#     r0=[]
# print(sol)
# k="11101101"
# m=len(k)
# dat=[]
# for i in range(m):
#     dat.append(k[i])
# # dat=dat[::-1]
# print(dat)
# for i in range(m):
#     if m+i+1<=pow(2,i):
#         break
#     else:
#         pass
# r=i
# # print(r)
# total=[None]*(m+r)
# print(total)
# for i in range(r):
#     if (m+r)-pow(2,i)==(m+r-1):
#         total[m+r-1]=0
#     else:
#         total=total[:(m+r)-pow(2,i)]+['0']+total[(m+r)-pow(2,i)+1:]
# i=0
# j=0
# while i<(len(dat)) and j<len(total):
#     if total[j]==None:
#         total[j]=dat[i]
#         i+=1
#         j=+1
#     else:
#         j+=1
# tot=[1,1,1,0,0,1,1,0,0,1,0,0]
# r=4
# m=8
# sum=0
# r0=[]
# sol=[]
# for i in range (r):
#     k=pow(2,i)
#     i1=0
#     l=k
#     while l<r+m:
#         if i1<k:
#             r0.append(1)
#             i1+=1
#             l+=1
#         elif i1==k:
#             for i1 in range(k-1,-1,-1):
#                 l+=1
#     for q in r0:
#         sum+=tot[q]
#     if q%2==0:
#         sol.append(0)
#     else:
#         sol.append(1)
    
#     r0=[]
# print(sol)



# print(total)


# ele=list(map(str,input().split(' ')))
# print(ele)
# i="He"
# k=((ord(i[:1]))-65)+10
# print(k)

# def compute_hcf(x, y):

# # choose the smaller number
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x % i == 0) and (y % i == 0)):
#             hcf = i 
#     return hcf

# num1 = 24
# num2 = 12

# print("The H.C.F. is", compute_hcf(num1, num2))


# def hcf(i,j):
#   if i>j:
#     t=j
#   else:
#     t=i
#   for a in range(1,t+1):
#     if(i%a==0)and(j%a==0):
#       h=a
#   return (a)


# ele=list(map(str,input().split(' ')))
# temp=[]
# for i in ele:
#   if len(i)>1:
#     k=((ord(i[:1]))-65)+10
#     m=((ord(i[1:2]))-97)+36
#     n=m+1
#     l=n*k+m
#     temp.append(l)
#   else:
#     l=((ord(i[:1]))-65)+10
#     temp.append(l)
# print(temp)
# temp1=[]
# for i in range(len(temp)):
#   for j in range(i+1,len(temp)):
#     h=hcf(temp[i],temp[j])
#     temp1.append(h)
# print(temp1)
# print(max(temp1))



# H O C N Au Ag Cl


# from re import T

# def hcf(x, y):
    
#     if i>j:
#         t=j
#     else:
#         t=i
#     for a in range(1,t+1):
#         if((i % a == 0) and (j % a == 0)):
#             ham = a 
#     return ham

# ele=list(map(str,input().split(' ')))
# temp=[]
# for i in ele:
#   if len(i)>1:
#     k=((ord(i[:1]))-65)+10
#     m=((ord(i[1:2]))-97)+36
#     n=m+1
#     l=n*k+m
#     temp.append(l)
#   else:
#     l=((ord(i[:1]))-65)+10
#     temp.append(l)
# temp1=[]
# for i in range(len(temp)):
#   for j in range(i+1,len(temp)):
#     h=hcf(temp[i],temp[j])
#     temp1.append(h)
# print(max(temp1))

# def hcf(i,j):

# # choose the smaller number
#     if i>j:
#         t=j
#     else:
#         t=i
#     for a in range(1,t+1):
#         if((i%a==0) and (j%a==0)):
#             h=i 
#     return (h)

# ele=list(map(str,input().split(' ')))
# temp=[]
# for i in ele:
#   if len(i)>1:
#     k=((ord(i[:1]))-65)+10
#     m=((ord(i[1:2]))-97)+36
#     n=m+1
#     l=n*k+m
#     temp.append(l)
#   else:
#     l=((ord(i[:1]))-65)+10
#     temp.append(l)
# temp1=[]
# for i in range(len(temp)):
#   for j in range(i+1,len(temp)):
#     h=hcf(temp[i],temp[j])
#     temp1.append(h)
# print(max(temp1))
        
# def hcf_(x,y):
#   while (y):
#     x,y=y,x%y
#   return(x)

# ele=list(map(str,input().split(' ')))
# temp=[]
# for i in ele:
#   if len(i)>1:
#     k=((ord(i[:1]))-65)+10
#     m=((ord(i[1:2]))-97)+36
#     n=m+1
#     l=n*k+m
#     temp.append(l)
#   else:
#     l=((ord(i[:1]))-65)+10
#     temp.append(l)
# temp1=[]
# for i in range(len(temp)):
#   for j in range(i+1,len(temp)):
#     h=hcf_(temp[i],temp[j])
#     temp1.append(h)
# o=max(temp1)
# print(str(o))









# def hcf_(i,j):
#   while (j):
#     i,j=j,i%j
#   return(i)

# ele=list(map(str,input().split(' ')))
# temp=[]
# if len(ele)>1:

#     for i in ele:
#         if len(i)>1:
#             k=((ord(i[:1]))-65)+10
#             m=((ord(i[1:2]))-97)+36
#             n=m+1
#             l=n*k+m
#             temp.append(l)
#         else:
#             l=((ord(i[:1]))-65)+10
#             temp.append(l)
# if len(ele)==1:
#     for i in ele:
#         if len(i)>1:
#             k=((ord(i[:1]))-65)+10
#             m=((ord(i[1:2]))-97)+36
#             n=m+1
#             l=n*k+m
#             temp.append(l)
#         else:
#             l=((ord(i[:1]))-65)+10
#             temp.append(l)
# print(temp)
# temp1=[]
# if len(temp)>1:

    
#     for i in range(len(temp)):
#         for j in range(i+1,len(temp)):
#             h=hcf_(temp[i],temp[j])
#             temp1.append(h)
# if len(temp)==1:
#     temp1.append(1)
# print(temp1)
# print(max(temp1),end="")

# def hcf_(i,j):
#   while (j):
#     i,j=j,i%j
#   return(i)

# ele=list(map(str,input().split(' ')))
# temp=[]
# for i in ele:
#   if len(i)>1:
#     k=((ord(i[:1]))-65)+10
#     m=((ord(i[1:2]))-97)+36
#     n=m+1
#     l=n*k+m
#     temp.append(l)
#   else:
#     l=((ord(i[:1]))-65)+10
#     temp.append(l)
# temp1=[]
# for i in range(len(temp)):
#   for j in range(i+1,len(temp)):
#     h=hcf_(temp[i],temp[j])
#     temp1.append(h)
# print(max(temp1),end="")




# def hcf_(x,y):
#   while (y):
#     x,y=y,x%y
#   return(x)




# x=626
# y=1039
# k=hcf_(x,y)
# print(k)




# ele=list(map(str,input().split(' ')))
# temp=[]
# if len(ele)>1:

#     for i in ele:
#         if len(i)>1:
#             k=((ord(i[:1]))-65)+10
#             m=((ord(i[1:2]))-97)+36
#             n=m+1
#             l=n*k+m
#             temp.append(l)
#         else:
#             l=((ord(i[:1]))-65)+10
#             temp.append(l)
# print(temp)







# Activity=[[1,2,100],[2,1,19],[3,2,27],
#         [4,1,25],[5,1,15]]
# Activity.sort(key = lambda x : x[2],reverse=True)
# print(Activity[3][2])



# import numpy as npp
# # from openpyxl import NUMPY


# n=int(input("enter the number of rows :"))
# a=[]

# for i in range(n*3):
#         k=int(input("enter the number :")) 
#         a.append(k)
# a1=npp.reshape(a,(4,3))
# print(a1)
# a=pow(1.004025,120)
# k=a*1000
# b=pow(1.0483,25)
# a*=1000
# a=int(a)
# b=int(pow(1.0483,10))
# c=a*48.3*25
# k+=c
# print(int(k))
# b=a*12
# c=b-12
# print(c)



# a=[10,20,30,40,50,60,70,80,90,100]
# print(a.index(40))


# k=math.floor(math.log(15))
# print(k)










# k=int(input("enter the number : "))
# k=str(k)
# arr=[]
# for i in k:
#     arr.append(i)
# # arr=int(arr)
# sum=0
# for i in arr:
#     sum=sum+int(i)

# print(sum)







##wipro_1##


# k=int(input("enter the umber : "))
# k=str(k)
# count=len(k)
# arr=[0]*count
# for i in range(count):
#     arr[i]=int(k[i])
# sum=0
# for i in range(count):
#     s=arr[i]*(i+1)
#     sum+=s
# print(sum)


##wipro_2##

# k=int(input("enter the umber : "))
# k=str(k)
# count=len(k)
# arr=[0]*count
# for i in range(count):
#     arr[i]=int(k[i])
# sum=0
# for i in range(count):
#     if i==(count-1):
#         s=arr[i]**0
#         sum+=s
#     else:

#         s=arr[i]**arr[i+1]
#         sum+=s
# print(sum)


##wipro_3##


# count=1
# c=0
# temp=0
# i=0
# a=[11,3,1,4,7,8,12,2,3,7]
# while i<(len(a)):
    
#     # i=(i-1)+temp-1
#     if i<len(a)-1:
#         if a[i]>a[i+1]:
#             count+=1
#             for j in range(i+1,len(a)):
#                 if a[j]>a[j+1]:
#                     count+=1
#                 else:
#                     c+=1
#                     break
#             i=j
#         i+=1
#         if temp<count:
#             temp=count
#         count=1
#     else:
#         break
                
# print(temp,c)


##wipro4##

# n = int(input()) 
# arr = []
# for i in range(n):
#     arr.append([j for j in input().split()])
    
# print(arr)

# Python program for transitive closure using Floyd Warshall Algorithm
#Complexity : O(V^3)

# from collections import defaultdict

# #Class to represent a graph
# class Grap:

# 	def __init__(self):
# 		self.V = 4

# 	# A utility function to print the solution
# 	def printSolution(self, reach):
# 		print ("Following matrix transitive closure of the given graph ")
# 		for i in range(self.V):
# 			for j in range(self.V):
# 				if (i == j):
# 				print ("%7d\t" % (1),end=" ")
# 				else:
# 				print ("%7d\t" %(reach[i][j]),end=" ")
# 			print()
	
	
# 	# Prints transitive closure of graph[][] using Floyd Warshall algorithm
# 	def transitiveClosure(self,graph):
# 		'''reach[][] will be the output matrix that will finally
# 		have reachability values.
# 		Initialize the solution matrix same as input graph matrix'''
# 		reach =[i[:] for i in graph]
# 		'''Add all vertices one by one to the set of intermediate
# 		vertices.
# 		---> Before start of a iteration, we have reachability value
# 		for all pairs of vertices such that the reachability values
# 		consider only the vertices in set
# 		{0, 1, 2, .. k-1} as intermediate vertices.
# 		----> After the end of an iteration, vertex no. k is
# 		added to the set of intermediate vertices and the
# 		set becomes {0, 1, 2, .. k}'''
# 		for k in range(self.V):
			
# 			# Pick all vertices as source one by one
# 			for i in range(self.V):
				
# 				# Pick all vertices as destination for the
# 				# above picked source
# 				for j in range(self.V):
					
# 					# If vertex k is on a path from i to j,
# 					# then make sure that the value of reach[i][j] is 1
# 					reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

# 		return(self.printSolution(reach))
		
# g=Grap()


# graph = [[1, 1, 0, 1],
# 		[0, 1, 1, 0],
# 		[0, 0, 1, 1],
# 		[0, 0, 0, 1]]

# #Print the solution
# g.transitiveClosure(graph)

#This code is contributed by Neelam Yadav



# a=[21,34,22,78,45,2,4,90]
# b=sorted(a)
# for i in range(len(b)):
# 	if b[0]==a[i]:
# 		k1=i
# for i in range(len(b)):
# 	if b[len(a)-1]==a[i]:
# 		k2=i
# if k2>k1:
# 	print(k2-k1)
# else:
# 	print(k1-k2)
# print("enter the values of a b c :")
# a,b,c=list(map(int, input().split(" ")))
# print(a)
# print(b)
# print(c)


a=[1,3,2,6,1,7,5]
b=[7,6,5,4,3,2,1]
sorted(a, key= lambda x: )




