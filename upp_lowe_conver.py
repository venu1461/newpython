# converting the lower to upper or upper to lower based on character count 
s=input("enter a string with combination of capital small letters:")
low_cnt=0
upp_cnt=0
for ch in s:
    if 'A'<=ch<='Z':
        upp_cnt+=1
    elif 'a'<=ch<='z':
        low_cnt+=1
if(low_cnt>upp_cnt):
    s=s.lower()
else:
    s=s.upper()
print(s)
