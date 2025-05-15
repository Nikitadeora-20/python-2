# def sum(arr,target):
#     arr.sort()
#     left , right =0 , len(arr)-1
#     while left < right:
#         sum = arr[left]+arr[right]
#         if sum==target:
#             return True
#         elif  sum < target:
#             left +=1
#         else:
#             sum > target
#             right -=1
#     return False

# if __name__ == "__main__":
#     arr=[1,2,3,5,7,10,11,15]
#     target = 0
    
#     if sum(arr,target):
#         print("true")
#     else:
#         print("false")                
    

# def triplet(arr,target):
#     arr.sort()
#     n= len(arr)
#     for i in range(n-2):
#         left = i+1
#         right = n-1
#         while left < right :
    
#             sum = arr[i]+arr[left]+arr[right]
#             if sum ==target:
#                 return  arr[i],arr[left],arr[right]
     
#             elif sum >target:
#                 right -=1
#             else:
#                 sum <target
#                 left +=1
        
#     return None        
# if __name__=="__main__":
#     arr=[1,2,3,5,7,10,11,15]
#     target=15
#     result = triplet(arr,target)
#     if result:
#         print("triplets",result)
#     else:
#         print("none ")    

    
def moveszero(nums):
    n=len(nums)
    left = 0 
    for right in range(n):
        if nums[right] != 0:
            nums[left],nums[right]=nums[right],nums[left]
            left +=1

if __name__ == "__main__":
    nums=[0,1,0,3,12]
    moveszero(nums)
    print("moves all zeroes to end",nums)        