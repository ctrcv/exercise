# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k <= 0:
            return []
        # write code here
        import heapq
        hp = []

        for i in tinput:
            if len(hp) == k:
                if -i > hp[0]:
                    heapq.heapreplace(hp, -i)
            else:
                heapq.heappush(hp, -i)
        return sorted([- j for j in hp])


inp = [4, 5, 1, 6, 2, 7, 3, 8]
k = 10
print(Solution().GetLeastNumbers_Solution(inp, k))
