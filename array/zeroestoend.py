def zeroes(arr):
    n=len(arr)
    if len(arr) == 1:
        return
    i=0
    while i< len(arr):
        if arr[i]==0:
            break
        i+=1

    if i == len(arr):
        return 
    j= i+1

    while j < len(arr):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1

arr=[1,0,2,4,5,0,0,3,5,1]
zeroes(arr)
print(arr)                            