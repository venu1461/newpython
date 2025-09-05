# matrics subtraction with user input
rows=int(input("enter no of rows="))
col=int(input("enter no of columns="))

print("enter the matrics1 values")
matrics1=[[int(input()) for i in range(rows)]for j in range(col)]
print("matrics1")
for i in range(rows):
    for j in range(col):
        print(format(matrics1[i][j],"<2"),end="")
    print()
 
print("enter matrics2 values:")
matrics2=[[int(input()) for i in range(rows)]for j in range(col)]
print("matrics2")
for i in range(rows):
    for j in range(col):
        print(format(matrics2[i][j],"<2"),end="")
    print()
    
    
result=[[0 for i in range(rows)] for j in range(col)]
for i in range(rows):
    for j in range(col):
        result[i][j]=matrics1[i][j] - matrics2[i][j]
print("result")       
for i in range(rows):
    for j in range(col):
        print(format(result[i][j],"<3"),end="")
    print()

#matrics1=[[1,1],[1,1]]
#matrics2=[[1,1],[1,1]]
# output [[0,0],[0,0]]