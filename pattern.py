def pattern(n):
    for i in range(1,n):
        for j in range(1,n):
            if (i+j)%2==1:
                print(0,end=" ")
            else:
                print(1,end=" ")
        print()
print(pattern(5))