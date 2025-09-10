def nozerointegers(n):
    for i in range(1,n):
        j=n-i
        # if '0' not in str(i) and '0' not in str(j):
        if i%10!=0 and j%10!=0:
            return [i,j]
print(nozerointegers(500))
# def nozero(n):
#     def is_no_zero(x):
#         return '0' not in str(x)
#     for i in range(1,n):
#         j=n-i
#         if is_no_zero(i) and is_no_zero(j):
#             return [i,j]
# print(nozero(1010))