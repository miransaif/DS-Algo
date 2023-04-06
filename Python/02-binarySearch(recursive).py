# TC : O(logn)

#functionality
def binarySearch(arr, target, low, high):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binarySearch(arr, target, mid+1, high)
        else:
            return binarySearch(arr, target, low, mid-1)
    
    return -1



#driver code

arr = [20, 30, 40, 50, 60, 70, 80, 90]
target = 90
low = 0
high = len(arr)-1
result = binarySearch(arr, target, low, high)
print(result)