# PS: You are a product manager and currently leading a team to develop a new product.
    # Unfortunately, the latest version of your product fails the quality check. Since each
    # version is developed based on the previous version, all the versions after a bad version
    # are also bad. Suppose you have n version and you want to find out the first bad one,
    # which causes all the following ones to be bad. Also, talk about the time complexity of
    # your code.
    # Test Cases:
    # Input: [0,0,0,1,1,1,1,1,1]
    # Output: 3
    # Explanation: 0 indicates a good version and 1 indicates a bad version. So, the index of
    # the first 1 is at 3. Thus, the output is 3

# Time Complexity = O(log n)

# function def
def findBadversion(arr,low,high,target):
    while low <= high:
        mid = low + (high-low)//2
        if target == arr[mid]:
            if arr[mid-1] == 0:
                return mid
            else:
                high = mid-1
        else:
            low = mid+1
    return -1


# driver code
arr = [0,0,0,1,1,1,1,1,1]
target = 1
low = 0
high = len(arr)-1
result = findBadversion(arr,low,high,target)
print(result)