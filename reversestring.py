# this is in built function
# s=input("enter the string")
# x=s[::-1]
# print(x)

# this is normal
s=input("enter the string")
ch=" "
for i in s:
    ch=i+ch
print(ch)