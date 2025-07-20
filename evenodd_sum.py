# find the even_sum and odd_sum of numbers based on index  in the given array
n=[1,2,3,4,5,6]
even_sum=0
odd_sum=0
for i in range(len(n)):
    if i%2==0:
        even_sum+=n[i]
    else:
        odd_sum+=n[i]
print(even_sum)
print(odd_sum)