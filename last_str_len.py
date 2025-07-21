# def length_string(s):
#     words=s.strip().split()
#     if not words:
#         return 0
#     return len(words[-1])
# s="hello world"
# print(length_string(s))

# s="hello world"
# print(len(s.strip().split()[-1]))

def length_os_last_word(s):
    s=s.strip()
    length=0
    for  char in s:
        if char == ' ':
            length = 0
        else:
            length+=1
    return length
s='hello world'
print(length_os_last_word(s))