
def quickSort(nums, left=None, right=None):
    if left < right:
        partitionIndex = partition(nums, left, right )
        quickSort(nums, left, partitionIndex - 1)
        quickSort(nums, partitionIndex + 1, right)

    return nums


def partition(nums, left, right):
    pivot = nums[left]
    i, j = left, right

    while i < j:
        while nums[j] >= pivot and i < j:
            j -= 1
        while nums[i] <= pivot and i < j:
            i += 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[left], nums[i] = nums[i], pivot
    return i


numbers = [-5, 5, 11, 2, 4, -3]
print(quickSort(numbers, 0, len(numbers) - 1))
