# PS :Given a positive integer num, write a program that returns True if num is a perfect
    # square else return False. Do not use built-in functions like sqrt. Also, talk about the time
    # complexity of your code.
    # Test Cases:
    # Input: 16
    # Output: True
    # Input: 14
    # Output: False

# TC = O(log n)

# function def
def isPerfectSquare(num):
    low =1
    high = num
    if num == 1:
        return True
    while (high-low)>1:
        mid = low + (high-low)//2
        if mid*mid == num:
            return True
        elif mid*mid>num:
            high = mid-1
        elif mid*mid<num:
            low = mid+1
        if low*low == num or high*high == num:
            return True
    return False

# driver code
num = int(input("enter a number: "))
result = isPerfectSquare(num)
print(result)
