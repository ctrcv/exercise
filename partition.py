from random import randint


def partition(arr, start, end):
    pivotIndex = randint(start, end)
    pivotValue = arr[pivotIndex]
    arr[end], arr[pivotIndex] = arr[pivotIndex], arr[end]
    storeIndex = start
    # print('pivot index', pivotIndex, pivotValue)
    while start < end:
        if arr[start] < pivotValue:
            arr[storeIndex], arr[start] = arr[start], arr[storeIndex]
            storeIndex += 1
        start += 1
        print(arr)

    arr[storeIndex], arr[end] = arr[end], arr[storeIndex]
    # print(arr)
    return storeIndex


nums = [2, 6, 3, 4, 8, 62, 4, 32, 12, 5]
print(partition(nums, 0, len(nums) - 1))
