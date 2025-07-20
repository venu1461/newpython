# count the characters without space
str="v e n u go"
count=0
for i in range(len(str)):
    if str[i]!=' ':
        count+=1
print(count)