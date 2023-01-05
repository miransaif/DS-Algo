#functionality
def linearSearch(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1


#Dirvercode
arr = [20, 45, 27, 47, 55, 67, 75, 88, 90]
target = 67
result = linearSearch(arr, target)
print(result)