def subsequences_with_sum_k(arr, k, index=0, current=[], current_sum=0):
    if index == len(arr):
        if current_sum == k:
            print(current)
        return

    # Include current element
    subsequences_with_sum_k(arr, k, index + 1, current + [arr[index]], current_sum + arr[index])

    # Exclude current element
    subsequences_with_sum_k(arr, k, index + 1, current, current_sum)

# Example usage
arr = [1, 2, 1]
k = 3
subsequences_with_sum_k(arr, k)
