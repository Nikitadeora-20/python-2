# #merge 2 sorted array
# def sortedarray(arr1, arr2):
#     i = j = 0
#     result = []

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1

#     # Add remaining elements
#     while i < len(arr1):
#         result.append(arr1[i])
#         i += 1

#     while j < len(arr2):
#         result.append(arr2[j])
#         j += 1

#     return result

# arr1=[1,2,4]
# arr2=[1,3,4]
# result=sortedarray(arr1,arr2)
# print(result)


#merge two sorted array without repeat duplicates
def sortedarray(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = j = 0
    result = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:  # arr1[i] == arr2[j]
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements from arr1
    while i < n:
        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < m:
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result
arr1=[1,2,4]
arr2=[1,3,4]
result=sortedarray(arr1,arr2)
print(result)
