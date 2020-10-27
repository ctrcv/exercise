from typing import List


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     from collections import Counter
    #     if not nums or k > len(nums) or k < 0:
    #         return []
    #
    #     topk = Counter(nums).most_common(k)
    #     return [topk[i][0] for i in range(len(topk))]

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = {}
    #     for num in nums:
    #         if num not in counter:
    #             counter[num] = 1
    #         else:
    #             counter[num] += 1
    #
    #     items = []
    #     for item in counter.items():
    #         items.append(item)
    #
    #     sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    #     print(sorted_items)
    #     res = [sorted_items[i][0] for i in range(k)]
    #     return res

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = {}
    #     for num in nums:
    #         if num not in counter:
    #             counter[num] = 1
    #         else:
    #             counter[num] += 1
    #
    #     sorted_cnter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    #     res = [sorted_cnter[i][0] for i in range(k)]
    #     return res

    # 桶排序
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     import collections
    #     counter = collections.Counter(nums)
    #     n = len(nums)
    #     c2 = [[] for _ in range(n + 1)]
    #     for v, c in counter.items():
    #         c2[c].append(v)
    #     print(c2)
    #     res = []
    #     for i in range(n, -1, -1):
    #         res.extend(c2[i])
    #         if len(res) == k:
    #             return res

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = dict()
    #     for num in nums:
    #         if num not in counter:
    #             counter[num] = 1
    #         else:
    #             counter[num] += 1
    #
    #     n = len(nums)
    #     memo = [[] for _ in range(n + 1)]
    #     for key, val in counter.items():
    #         memo[val].append(key)
    #     # print(memo)
    #
    #     res = []
    #     for i in range(n, -1, -1):
    #         if memo[i]:
    #             res.extend(memo[i])
    #         if len(res) == k:
    #             return res

    # 维护大小为k的堆： 在本地结果正确，但leetcode上运行时测试例3返回错误
    # 输出：[-1， 4], 预期：[-1, 2]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        counter = Counter(nums)
        heap = []
        res = []
        for key, val in counter.items():
            if len(heap) == k:
                if heap[0][1] < val:
                    heapq.heapreplace(heap, (key, val))
            else:
                heapq.heappush(heap, (key, val))

        # print(heap)
        while heap:
            # res.append(heap.pop()[0])
            res.append(heapq.heappop(heap)[0])
        return res


# nums = [1, 1, 1, 2, 2, 3, 5]
# k = 2
# nums = [1]
# k = 1
nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
res = Solution().topKFrequent(nums, k)
print(res)
