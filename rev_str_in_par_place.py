def reverse_string(s,k):
    s=list(s)
    n=len(s)
    for i in range(0,n,2*k):
        s[i:i +k]=reversed(s[i:i+k])
    return ''.join(s)
k=2
s="abcdefgh"
print(reverse_string(s,k))  

# output:"badcfehg"