# def maximumsubarray(arr):
#     n=len(arr)
#     max_i =float('-inf')
#     for i in range(0,n):
#         total=0
#         for j in range(i,n):
#             total += arr[j]
#             max_i = max(max_i,total) 
#         return max_i

# arr=[-2,1,-4,6,2,1,-5,4]
# result=maximumsubarray(arr)
# print(result)            

def maximumsubarray(arr):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            max_sum = max(max_sum, total)
    return max_sum
arr = [-2, 1, -4, 6, 2, 1, -5, 4]
result = maximumsubarray(arr)
print(result)