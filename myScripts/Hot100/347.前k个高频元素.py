from typing import List
import heapq
#
# 在本地和leetcode上输出结果不一样呢,
# 在测试用例nums = [4, 1, -1, 2, -1, 2, 3], k=2时，本地输出[-1,2],而leetcode上得到的结果却是[-1,4]？
# 原因是heapq.heappush(heap, (key, cnt))和heapq.heapreplace(heap, (key, cnt))压入语句存在问题(程序已更新)
# 因为压入的数据是一对数据的元组,压入堆中无法直接对比元组数据的大小,无法进行堆排序,导致更新时出现错误
# python3.6出现结果为[-1,4]的原因预计是这样,默认是对第一个元素进行排序处理,将压入堆的数据顺序更改后输出正确
# 而本地运行的python3.5运行结果正确的原因暂未知

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 哈希表+堆排序
        # 先使用哈希表建立频次表,再根据频次建立大小为k的堆;遍历频次数组O(N),堆操作O(logk),所以时间复杂度O(nlogk)

        # 统计频次
        count = {}
        heap, res = [], []
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # 建立大小为k的小顶堆
        for key, cnt in count.items():
            if len(heap) < k:
                # heapq.heappush(heap, (cnt, key))
                heapq.heappush(heap, (key, cnt))
            else:
                # if cnt > heap[0][0]:
                if cnt > heap[0][1]:
                    # heapq.heapreplace(heap, (cnt, key))
                    heapq.heapreplace(heap, (key, cnt))
        # print(heap)
        # 读取堆
        for _ in range(len(heap)):
            top = heapq.heappop(heap)
            res.append(top[0])
            # res.append(top[1])

        return res


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # 2. 桶排序
#         # 先统计频次,然后使用频次作为数组的下标
#         # 时间复杂度和空间复杂度O(N)
#
#         count = {}
#         max_cnt = 0  # 确定数组长度
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
#             max_cnt = max(count[num], max_cnt)
#
#         # 可能会出现相同频次的数字,所以每个频次下对应位置使用列表存储数据
#         arr = [[] for _ in range(max_cnt)]
#         for key, cnt in count.items():
#             arr[cnt - 1].append(key)
#         # print(arr)
#         res = []
#         for i in range(max_cnt-1, -1, -1):
#             if len(res) >= k:
#                 return res
#             res.extend(arr[i])
#         # print(res)
#         return res


# Nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
# Nums = [1, 1, 1, 2, 2, 3]
Nums = [4, 1, -1, 2, -1, 2, 3]
# Nums = [4]
K = 2
# Nums = [-1,-1]
# K = 1
print("测试用例:", Nums)
print(Solution().topKFrequent(Nums, K))
