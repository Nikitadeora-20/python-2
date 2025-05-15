def array(arr):
    n=len(arr)
    for i in range(0,n):
        if arr[i]>arr[i+1]:
            return False

        else:
            arr[i] < arr[i+1]
            return True


arr=[3,5,6,7,8,9,10]
result=array(arr)
print(result)                      