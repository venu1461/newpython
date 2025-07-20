n=int(input("enter a nummber"))
rev=0
while (n!=0):
    temp = n % 10
    rev=rev*10+temp
    n//=10
print(rev)

# another way

# n=input()
# reverse_string=int(str(n[::-1]))
# print(reverse_string)