# PS : In a 2d Array find the element
# TC : O(log(m*n))

# function defination
def search2DArray(target):
    # number of rows
    m = len(arr)
    if m == 0:
        return False
    # number of columns
    n = len(arr[0])
    left, right = 0, m*n-1
    # binary search implementation
    # row = mid//n
    # column = mid%n
    while left <= right:
        mid = left + (right-left)//2
        mid_element = arr[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1
    return False


# driver code 
arr = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
target = 3
result = search2DArray(target)
print(result)