# factorial using recursion 
# def factorial(nums):
#     if nums==0 or nums==1:
#         return 1
#     print(nums)
#     return nums*factorial(nums-1)

# factorial(5)        


#reverse array using recursion 

# def func(arr,left,right):
    
#     if left>=right:
#         return
#     arr[left],arr[right]=arr[right],arr[left]
#     func(arr,left+1,right-1) 

# def reversearray(arr,left,right):
#     func(arr,left,right)       
#     return arr

# arr=[5,9,8,3,6,7,1,4,2]
# reverse_array = reversearray(arr,0,len(arr)-1)
# print(arr)


#check if string is palindrome using recursion 

# def func(s,l,r):
#     if l >=r:
#         return True
#     if s[l]!=s[r]:
#         return False
#     return func(s,l+1,r-1)

# s="anbcddcbna"
# result =func(s,0,len(s)-1)
# print("palindrome" if result else "not palindrome")


#fibonacci number using recursion

def func(nums):
    if nums ==0 or nums==1:
        return nums
    return func(nums-1)+func(nums-2)

print(func(7))
