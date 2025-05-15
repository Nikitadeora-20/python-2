def s_largest(arr):
    n=len(arr)
    largest=float('-inf')
    s_largest=float('-inf')

    for i in range(0,n):
        if arr[i]>largest:
            s_largest=largest
            largest=arr[i]

        elif arr[i]>s_largest and arr[i]!=largest:
            s_largest=arr[i]

    return s_largest

arr=[55,32,97,-55,45,32,88,21]
result=s_largest(arr)
print(result)                