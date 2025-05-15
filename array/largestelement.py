def largest(arr):
    n=len(arr)
    largest=arr[0]
    for i in range (0,n):
        if arr[i]>largest:
            largest=arr[i]
        largest=max(largest,arr[i])
       
    return largest

arr=[55,32,-97,99,3,67]
result=largest(arr)
print(result)            
         