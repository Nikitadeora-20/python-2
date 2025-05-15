def remaining(arr,n):
    if(n==1):
        return arr[0]

    arr.sort()
    return arr[(n-1)//2]

arr=[1,5,4,2,6]
n=len(arr)
print(remaining(arr,n))        