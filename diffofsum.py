# find the difference of sum(n,m) sum number Not divisible n and divisible by n
n=int(input("enter a number :"))
m=int(input("enter a number :"))
sum1=0
sum2=0
if n == 0:
    print("error")
else:
    for i in range(1,m+1):
        if (i % n == 0): 
            sum1 += i
        else:
            sum2 += i
    
print(sum1)
print(sum2)

    
    