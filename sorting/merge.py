def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=mergesort(arr[:mid])
    right_half=mergesort(arr[mid:])
    
    return merge_array(left_half,right_half)

def merge_array(left,right):
    result=[]
    i=0
    j=0
    n=len(left)
    m=len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i]) 
            i+=1

        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result    
        

arr=[3,5,6,4,8,9,10,7,1]
result=mergesort(arr)
print(result)              


#decending 

def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=mergesort(arr[:mid])
    right_half=mergesort(arr[mid:])
    
    return merge_array(left_half,right_half)

def merge_array(left,right):
    result=[]
    i=0
    j=0
    n=len(left)
    m=len(right)
    while i<n and j<m:
        if left[i]>=right[j]:
            result.append(left[i]) 
            i+=1

        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result    
        

arr=[3,5,6,4,8,9,10,7,1]
result=mergesort(arr)
print(result)              

