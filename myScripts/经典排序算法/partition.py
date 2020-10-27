import random


def partition(data, start, end):
    print(data)
    idx = random.randint(start, end)
    print('pivot idx: ', idx)
    data[idx], data[end] = data[end], data[idx]
    print('after swap: ', data)
    small = start - 1
    for idx in range(start, end):
        if data[idx] < data[end]:
            small += 1
            if small != idx:
                data[idx], data[small] = data[small], data[idx]

        print('第%d次循环：' % idx, 'data:', data, 'small: ', small)

    small += 1
    data[small], data[end] = data[end], data[small]
    print(data)
    return small


nums = [2, 8, 21, 4, 2, 5, 3, 5, 7]
print(partition(nums, 0, len(nums) - 1))
