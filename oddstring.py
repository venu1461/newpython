n=int(input("enter array length"))
A=[]
for i in range(n):
    A.append(int(input(f"enter values{i+1}:")))
labels=[]
for num in A:
    if num%2==0:
        labels.append("even")
    else:
        labels.append("odd")
label_string=" ".join(labels)
print(label_string)     # it will print evenoddevenodd likethat