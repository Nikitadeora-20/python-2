#ascending 
def bubblesort(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        swapped = False
        for j in range (0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr 

arr=[1,5,6,2,4,8,9]
result=bubblesort(arr)
print(result)              

#descending 
def bubblesort(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        swapped = False
        for j in range (0,i+1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr 

arr=[1,5,6,2,4,8,9]
result=bubblesort(arr)
print(result)              
