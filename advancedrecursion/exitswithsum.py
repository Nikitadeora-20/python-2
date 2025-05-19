def exists_subsequence_with_sum_k(arr, k, index=0, current_sum=0):
    # Base case: if current_sum == k
    if current_sum == k:
        return True
    # If we reach the end of the array
    if index == len(arr):
        return False

    # Include current element
    if exists_subsequence_with_sum_k(arr, k, index + 1, current_sum + arr[index]):
        return True

    # Exclude current element
    if exists_subsequence_with_sum_k(arr, k, index + 1, current_sum):
        return True

    return False

# Example usage
arr = [1, 2, 3]
k = -1

if exists_subsequence_with_sum_k(arr, k):
    print(f"A subsequence with sum {k} exists.")
else:
    print(f"No subsequence with sum {k} exists.")
