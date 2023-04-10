# PS: Compute and return the square root of x, where x is guaranteed to be a non-negative
    # integer. And since the return type is an integer, the decimal digits are truncated and only
    # the integer part of the result is returned. Also, talk about the time complexity of your
    # code.
    # Test Cases:
    # Input: 4
    # Output: 2
    # Input: 8
    # Output: 2
    # Explanation: The square root of 8 is 2.8284…., the decimal part is truncated and 2 is
    # returned.
    # Hint: Try to use a modified binary search approach for an optimized solution

# TC = O(log n)

# function def
def squareroot(num):
    low = 1
    high = num
    while low<=high:
        mid = low + (high-low)//2
        if mid*mid == num:
            return mid
        elif mid*mid > num:
            high = mid-1
        elif mid*mid < num:
            low = mid+1
            ans = mid
    return ans
# driver code 
num = int(input(('enter a number: ')))
result = squareroot(num)
print(result)