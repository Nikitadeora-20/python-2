def convert2binary(nums):
    if nums == 0:
        return "0"
        
    result = ""
    while nums > 0:
        if nums % 2 == 1:
            result += "1"
        else:
            result += "0"
        nums = nums // 2
    result = result[::-1]
    return result

# Test
nums = 13
result = convert2binary(nums)
print(result)
