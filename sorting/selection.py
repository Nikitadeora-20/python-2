#ascending selection sort
# def selectionsort(nums):
#     n=len(nums)
#     for i in range (0,n):
#         min_idx=i
#         for j in range(i+1,n):
#             if nums[j]<nums[min_idx]:
#                 min_idx=j
#         nums[i],nums[min_idx]=nums[min_idx],nums[i]
#     return nums    

# nums=[5,7,8,4,1,6,9,2]  
# result=selectionsort(nums)
# print(result)          


#desecending 

def selectionsort(nums):
    n=len(nums)
    for i in range(0,n):
        min_idx=i
        for j in range(i+1,n):
            if nums[j]>nums[min_idx]:
                min_idx=j
        nums[i],nums[min_idx]=nums[min_idx],nums[i]
    return nums   
nums=[5,7,8,4,1,6,9,2]
result = selectionsort(nums)
print(result)     