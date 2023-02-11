def factorialing(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

if __name__=='__main__':
    n=int(input("enter the number :"))
    factorialing(n)
