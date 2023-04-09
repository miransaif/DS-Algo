# TC : O(logn)

#functionality
def binarySearch(arr, target, low, high):
    while low <= high:
        mid = low+ (high-low)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid+1
        else:
            high = mid-1 
    
    return -1



#drivercode

arr = [20, 30, 40, 50, 60, 70, 80, 90]
target = 90
low = 0
high = len(arr)-1
result = binarySearch(arr, target, low, high)
print(result)