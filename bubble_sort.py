# sort the elements in the list 
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[64,34,25,12,22,11,90]
sorted_arr=bubble_sort(arr)
print(sorted_arr)

# output
#[11, 12, 22, 25, 34, 64, 90]