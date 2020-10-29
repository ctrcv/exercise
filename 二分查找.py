def binary_search_recursion(nums, val, low, high):
    """
    二分查找递归实现
    :param nums: 有序数组
    :return: val在nums中的索引
    """
    if high < low:
        return

    mid = (low + high) // 2
    if nums[mid] > val:
        return binary_search_recursion(nums, val, low, mid - 1)
    elif nums[mid] < val:
        return binary_search_recursion(nums, val, mid + 1, high)
    else:
        return mid


def binary_search_loop(nums, val, low, high):
    """
    二分查找循环实现
    :param nums:
    :param val:
    :param low:
    :param high:
    :return:
    """
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > val:
            high = mid - 1
        elif nums[mid] < val:
            low = mid + 1
        else:
            return mid
    return None


Nums = [2, 3, 4, 8, 10, 11]
Val = 11
print(binary_search_recursion(Nums, Val, 0, len(Nums)))
print(binary_search_loop(Nums, Val, 0, len(Nums)))

# 二分算法模块
from bisect import bisect_left, bisect_right
print(bisect_left(Nums, 11))
print(Nums)
print(bisect_right(Nums, 11))
print(Nums)
