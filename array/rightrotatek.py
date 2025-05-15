#using sliciing 
# def rotate(arr):
#     n=len(arr)
#     k=3
#     k= n%k
#     arr[:] = arr[n-k:] + arr[:n-k]

# arr=[5,-2,3,9,0,6,10,7]
# rotate(arr)
# print(arr)     

#without slicing
def reverse(arr,left,right):   
    while left < right:
        arr[left],arr[right]=arr[right],arr[left]
        left +=1
        right-=1

def rotate(arr,k):
    n=len(arr)
    k= k%n

    reverse(arr,n-k,n-1)#reverse last k element 
    reverse(arr,0,n-k-1)#reverse remaining array 
    reverse(arr,0,n-1)#whole array    


arr=[5,-2,3,9,0,6,10,7]
rotate(arr,3)
print(arr)     
