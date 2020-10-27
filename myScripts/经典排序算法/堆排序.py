def heapSort(arr):
    global arrlen
    arrlen = len(arr)
    buildMaxHeap(arr)
    for i in range(arrlen - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arrlen -= 1
        heapify(arr, 0)

    return arr


def buildMaxHeap(arr):
    mid = int(len(arr) / 2 + 0.5)
    for i in range(mid, -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < arrlen and arr[left] > arr[largest]:
        largest = left
    if right < arrlen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)


numbers = [-5, 5, 11, 2, 4, -3]
print(heapSort(numbers))
