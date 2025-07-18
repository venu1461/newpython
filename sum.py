# sum the array elements take from the user
n=int(input("enter the array length:"))
a=[]
sum=0
for i in range(n):
    a.append(int(input(f"enter the elements{i+1}:")))
for num in a:
    sum+=num
print(sum)
