# max element in the arrray
# s=[2,4,6,7,4,9,10]
# max=0
# for i in range(len(s)):
#     if s[i]>max:
#         max=s[i]
# print(max)


# reverse a number

# n=1234
# rev=0
# while(n!=0):
#     temp=n % 10
#     rev=rev*10 + temp
#     n//=10
# print(rev)


# import math

# def is_prime(num):
#     if num <=1:
#         return False 
#     for i in range(2, int(math.isqrt(num))+1):
#         if num % i == 0:
#             return False 
#     return True
# num=int(input())
# if is_prime(num):
#     print(f" {num} is a prime ")
# else:
#     print(f" {num} is not prime")


# s='a b b c d e'
# word_count={}
# for word in s .split():
#     word_count[word]=word_count.get(word,0)+1
# x=word_count[i] 
# print(word_count)


# def highest_frequency(n,arr):
#     frequency={}
#     for i in arr:
#         if i in frequency:
#             frequency[i]+=1
#         else:
#             frequency[i]=1
#     max_freq=0
#     item=" "
#     for i in arr:
#         if frequency[i]>max_freq:
#             max_freq=frequency[i]
#             item = i
#     print(item)
# n=int(input())
# arr=input().split()
# print(highest_frequency(n,arr))


# def sum_xor(n,a):
#     odd_sum=0
#     xor_even=0

#     for i in range(n):
#         if (i%2==0):
#             xor_even^=a[i]
#         else:
#             odd_sum+=a[i]
#     return odd_sum -xor_even
# n=int(input())
# a=list(map(int,input("enter a number").split()))
# result=sum_xor(n,a)
# print(result)


# import math
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(math.isqrt(n))+1):
#         if i%2 == 0:
#             return False
#     return True
# n=int(input("number:"))
# if is_prime(n):
#     print("true")
# else:
#     print('false')

# n=int(input("number"))
# fact=1
# if n <0:
#     print("it is negative")
# elif n == 0:
#     print(f"the factorial of{n} is 1")
# else:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)


# import random
# num=random.random() # it is used for range between 0 and 1
# num1=random.randint(1,100) # it is used in between range from n to n 
# num2=random.randrange(0,100,2) # gives random number  in a range with incremental steps
# num3=random.sample(range(1,100),5)  # gives a series of random numbers
# print(num)
# print(num1)
# print(num2)
# print(num3)

# fibnoci series
# n= int(input("enter a number"))
# a=0
# b=1
# if n <1:
#     print('null')
# elif n == 1:
#     print(a)
# elif n == 2:
#     print(a)
#     print(b)
# elif n >2:
#     print(a)
#     print(b)
#     for i in range(n-2):
#         c=a+b
#         a,b=b,c
#         print(c)
      
# def capital(string):
#     return string.capitalize()
# string='vENuGopalReddY'
# s=capital(string)
# print(s)


# arr=[2,4,6,77]
# value=77
# x=arr.index(value)  to find index value
# print(x)

# l1=[1,2,3,5,6]
# val=3
# k=0
# for i in range(len(l1)):
#     if (l1[i]!=val):
#         l1[k]=l1[i]
#         k+=1
# print(k)
# print(l1[:k])


# x=[1,2,3,4,5,6,4]
# v=4
# while v in x:
#     x.remove(v)
# print(x)
#  # Initial array
# nums = [3, 2, 2, 3]
# val = 3

# # Track index of where to place the next valid element
# k = 0

# # Loop through the array
# for i in range(len(nums)):
#     if nums[i] != val:
#         nums[k] = nums[i]
#         k += 1

# # Result
# print("Number of elements not equal to val:", k)
# print("Modified array (first k elements):", nums[:k])
       
    

# nums=[3,2,2,5,5,5,5,6,7,7,5,3]
# target=5
# x=[]
# target=5
# for i in nums:
#     if i == target:
#         x.append(i)
# print(len(x))


# k=0
# for i in nums:
#     if i != target:
#         nums[k]=i
#         k +=1
# print(nums[:k])

# nums=[1,3,4,5,3,2,1,2,3]
# nums=set(nums)
# print(len(nums))
# k=[]
# for i in range(len(nums)):  # find the length of unique values in the list
#     if i not in k:
#         k.remove(i)
#     else:
#         k.append(i)

# print(len(k))

# import math
# def square(x):
#     if x<0:
#         return 0
#     else:
#         return math.floor(x**0.5)
# x=81
# print(square(x))

# s="abcd"
# t="abchde"
# x=[]
# for i in t:
#     if i not in s:
#         x.append(i)
# print(''.join(x)) 
# print(len(x))
# # output he
# # 2
# def findTheDifference(s: str, t: str) -> str:
#     result = 0
#     for ch in s + t:
#         result ^= ord(ch)
#     return chr(result)
# from collections import Counter

# def findTheDifference(s: str, t: str) -> str:
#     count_s = Counter(s)
#     count_t = Counter(t)
#     for ch in count_t:
#         if count_t[ch] != count_s.get(ch, 0):
#             return ch
# def findTheDifference(s: str, t: str) -> str:
#     s_sorted = sorted(s)
#     t_sorted = sorted(t)
#     for ch_s, ch_t in zip(s_sorted, t_sorted):
#         if ch_s != ch_t:
#             return ch_t
#     return t_sorted[-1]

# binary search
# def binary_search(arr,left,right,target):
#     if left >right:
#         return False
#     mid=(left+right)//2         #binary search
#     if target == arr[mid]:
#         return mid
#     elif target >arr[mid]:
#         return binary_search(arr,mid+1,right,target)
#     else:
#         return binary_search(arr,left,mid-1,target)
# arr=[1,3,5,7,9,10]  
# result= binary_search(arr,0,len(arr)-1,7)        
# print(result)


# @binary_search
# def search(arr,target):
#     return binary_search(arr,0,len(arr)-1,target)

# arr=[1,3,5,7,9,10]
# target=7
# for i in range(len(arr)):  linear search
#     if arr[i]==target:
#         print(i)
#         break

# def next_greatest_letter(arr,left,right,target):
#     while left<=right:
#         mid=left+right//2
#         if arr[mid]<=target:
#             left=mid+1
#         else:
#             right=mid-1
#     return arr[left % len(arr)]
# arr=['c','f','j']
# print(next_greatest_letter(arr))

# matrix = [[1, 2], 
#           [3, 4]]
# matrix2=[[2,4],
#         [4,5]]
# rows=len(matrix)
# col=len(matrix[0])
# tran=[[0 for i in range(rows)] for j in range(col)]
# for i in range(rows):
#     for j in range(col):
#         tran[i][j]=matrix[i][j] + matrix2[i][j]
# print(matrix)
# print(matrix2)
# print(tran)

# import pandas as pd
# matrix =pd.DataFrame([[1,2],[3,4]])
# trans=matrix.T
# print(trans)

# n=175
# dis=0
# temp=n
# def find_position(data):
#     str_data=str(data)
#     return len(str_data)
# while temp!=0:
#     dis+=(temp%10)** find_position(temp)
#     temp//=10# removing the last elemet
# if dis==n:
#     print("yes")
# else:
#     print("no")



# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def mergeTwoLists(list1, list2):
#     dummy = ListNode()
#     tail = dummy

#     while list1 and list2:
#         if list1.val < list2.val:
#             tail.next = list1
#             list1 = list1.next
#         else:
#             tail.next = list2
#             list2 = list2.next
#         tail = tail.next

#     tail.next = list1 if list1 else list2
#     return dummy.next

# sol=Solution()
# list1 = [1,2,4]
# list2 = [1,3,4]
# print(sol.mergeTwoLists(list1,list2))

# def extra_sum(func):
#     def inner(x):
#         if x==x[::-1]:
#             print('Truee')
#         else:
#             print('nothing')
#     return inner
# @extra_sum
# def sum(a):
#     print(a)
# sum('120')


# multiple decorators and single function
def upper_d(func):
    def inner():
        str1= func()
        return str1.upper()
    return inner
def split_d(func):
    def wrapper():
        str2= func()
        return str2.split()
    return wrapper

@split_d
@upper_d
def process():
    return 'good morning'
print(process())