
def mergeSort(nums):
    n = len(nums)
    if n < 2:
        return nums

    mid = int(n / 2 + 0.5)
    left_arr, right_arr = nums[:mid], nums[mid:]
    return merge(mergeSort(left_arr), mergeSort(right_arr))


def merge(left_arr, right_arr):
    result = []
    while left_arr and right_arr:
        if left_arr[0] > right_arr[0]:
            result.append(right_arr.pop(0))
        else:
            result.append(left_arr.pop(0))

    if left_arr:
        result.extend(left_arr)
    if right_arr:
        result.extend(right_arr)

    return result


numbers = [-5, 5, 11, 2, 4, -3]
print(mergeSort(numbers))
