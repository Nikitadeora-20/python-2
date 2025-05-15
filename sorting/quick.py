#ascending 
def quick_sort(nums,low,high):
    if low<high:
        p_idx = partition(arr,low,high)
        quick_sort(arr,low,p_idx-1)
        quick_sort(arr,p_idx+1,high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr=[4,1,7,6,3,2,8]
quick_sort(arr,0,len(arr)-1)
print(arr)

#descending 

def quick_sort(nums,low,high):
    if low<high:
        p_idx = partition(arr,low,high)
        quick_sort(arr,low,p_idx-1)
        quick_sort(arr,p_idx+1,high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >=pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr=[4,1,7,6,3,2,8]
quick_sort(arr,0,len(arr)-1)
print(arr)

