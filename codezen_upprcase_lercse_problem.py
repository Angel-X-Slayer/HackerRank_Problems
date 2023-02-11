n=int(input(" "))
k=""
for i in range(n):
    a=[]
    s=input("")
    l=len(s)
    for i in range(l):
        if(i==0):
            if(ord(s[i])>=97):
                j=ord(s[i])-32
                j=chr(j)
                a.append(j)
            else:
                a.append(s[i])
        else:
            if(ord(s[i])<97):
                j=ord(s[i])+32
                j=chr(j)
                a.append(j)
            else:
                a.append(s[i])
    for i in range(len(a)):
        k=k+a[i]
    # print(k,end="\n")
for i in range(len(k)):
    if(ord(k[i])<97):
        j=i
        for l in range((i+1),len(k)):
            if(ord(k[l])<97):2
                print(k[j:l])
for i in range(len(k),0,-1):
    if(ord(k[i])<97):
        print(k[i:len(k)])
        break
                
    




     
    
        
                