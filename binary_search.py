def binary_search(arr,left,right,target):
    if left >right:
        return False
    mid=(left+right)//2
    if target == arr[mid]:
        return mid
    elif target >arr[mid]:
        return binary_search(arr,mid+1,right,target)
    else:
        return binary_search(arr,left,mid-1,target)
arr=[1,3,5,7,9,10]  
result= binary_search(arr,0,len(arr)-1,7)        
print(result)

# output 3