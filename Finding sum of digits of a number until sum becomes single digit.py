def finding_single_digit_sum(n):
    sum=0
    while n!=0:
        r=int(n%10)
        n=int(n/10)
        sum=sum+r
    if sum>9:
        finding_single_digit_sum(sum)
    else:
        print(sum)
        
n=int(input("enter the number :"))
 
finding_single_digit_sum(n)

