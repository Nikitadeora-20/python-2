#using slicing 

# def rotate(arr):
#     n = len(arr)
#     if n == 0:
#         return
#     arr[:] = arr[-1:] + arr[:-1]


# arr=[5,-2,3,9,0,6,10,7]
# rotate(arr)
# print(arr)    


#without slicing 
def rotate(arr):
    n=len(arr)
    temp=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]

    arr[0]=temp

arr=[5,-2,3,9,0,6,10,7]
rotate(arr)
print(arr)    
