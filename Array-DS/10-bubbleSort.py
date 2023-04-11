# TC : O(n^2)

# function def
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr


# driver code
arr = [20, 35, 47, 50, 60, 70]
result = bubbleSort(arr)
print(result)