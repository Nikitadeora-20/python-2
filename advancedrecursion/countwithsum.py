def count_subsequences_with_sum_k(arr, k, index=0, current_sum=0):
    if index == len(arr):
        return 1 if current_sum == k else 0

    # Include current element
    include = count_subsequences_with_sum_k(arr, k, index + 1, current_sum + arr[index])

    # Exclude current element
    exclude = count_subsequences_with_sum_k(arr, k, index + 1, current_sum)

    return include + exclude

# Example usage
arr = [1, 2, 1]
k = 5
count = count_subsequences_with_sum_k(arr, k)
print(f"Total subsequences with sum = {k}: {count}")
