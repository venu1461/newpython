# we need to find the missing number from the array
s=[1,2,4,5,3,7]
n=len(s)+1
total_sum=n*(n+1)//2        # formul is n*(n+1)//2
miss_c=total_sum-sum(s)
print(total_sum)
print(miss_c)





