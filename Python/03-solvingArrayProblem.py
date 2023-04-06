#Problem Statement : Array is sorted and find 2 numbers whose sum is 210 from arrary (2 pointer approach)
# TC : O(n)

# funtionality
def searchOperation(arr, low, high, target):
    while low <= high:
        if arr[low]+arr[high] == target:
            return(low, high)
        elif target < arr[low]+arr[high]:   
            high = high-1
        else:
            low = low+1
    return -1

# driver code

arr = [20, 40, 60, 80, 90, 120, 240]
low = 0
high = len(arr)-1
target = 210
result = searchOperation(arr, low, high, target)
print(result)