def minmax(arr):
    min_value = 0
    max_value =0
    n=len(arr)

    arr.sort()
    j=n-1
     
    for i in range(n-1):
        min_value += arr[i]
        max_value += arr[j]
        j-=1

    print(min_value,"",max_value)
arr=[12,89,66,90,54]

minmax(arr)