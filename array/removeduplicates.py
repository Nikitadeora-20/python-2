
def duplicate(arr):
    n = len(arr)
    if n == 0:
        return 0

    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]  # No need to swap

    return i + 1  # Number of unique elements

arr=[1,1,1,2,2,3,3,4,4,7,9,9,10]
result=duplicate(arr)
print(result)