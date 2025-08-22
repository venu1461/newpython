# check the number is prime or not


import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")
