# Ternary Search
# TC : O(log3(n))

# funtion defination
def ternarySearch(arr,low,high,target):
    mid1 = low+(high-low)//3
    mid2 = high-(high-low)//3
    while low<=high:
        if target == arr[mid1]:
            return mid1
        elif target == arr[mid2]:
            return mid2
        elif target < arr[mid1]:
            return ternarySearch(arr,low,mid1-1,target)
        elif target > arr[mid2]:
            return ternarySearch(arr,mid2+1,high,target)
        else:
            return ternarySearch(arr,mid1+1,mid2-1,target)
    return -1


# driver code 
arr = [20,25,47,56,59,63,65,79,82]
target = 56
low = 0
high = len(arr)-1
result = ternarySearch(arr,low,high,target)
print(result)