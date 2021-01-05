def missingNumber(nums):
    n = len(nums)
    res = n
    for i in range(n):
        res ^= i ^ nums[i]
    return res


Nums = [3, 0, 1]
print(missingNumber(Nums))