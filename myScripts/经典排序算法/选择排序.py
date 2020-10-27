def selectSort(nums):
    n = len(nums)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[idx]:
                idx = j

        if idx != i:
            nums[i], nums[idx] = nums[idx], nums[i]

    print(nums)
    return nums


numbers = [-5, 5, 11, 2, 4, -3]
selectSort(numbers)


