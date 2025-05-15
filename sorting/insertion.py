#ascending
def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]= key 

    return arr
arr=[3,5,6,4,8,9,10,7,1]
result=insertionsort(arr)
print(result)            

#descending 
def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]<key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]= key 

    return arr
arr=[3,5,6,4,8,9,10,7,1]
result=insertionsort(arr)
print(result)            

