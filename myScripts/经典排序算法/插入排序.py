def insertSort(nums):
    n = len(nums)
    for i in range(n):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
            print(nums)

        nums[j + 1] = tmp

    # print(nums)
    return nums


numbers = [-5, 5, 11, 2, 4, -3]
insertSort(numbers)



