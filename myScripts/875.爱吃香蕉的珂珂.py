from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 1. 暴力法，超时
        # maxp = max(piles)
        # for v in range(1, maxp):
        #     if self.canFinish(piles, v, H):
        #         return v
        #
        # return maxp

        # 2.二分查找，时间复杂度O（NlogW），N是香蕉堆的数量，W是最大堆的香蕉数量
        maxp = max(piles)
        left, right = 1, maxp + 1
        while left < right:
            # 防止溢出
            mid = left + (right - left) // 2
            if self.canFinish(piles, mid, H):
                right = mid
            else:
                left = mid + 1

        return left

    def canFinish(self, piles, speed, H):
        t = 0
        for p in piles:
            flag = 1 if p % speed > 0 else 0
            tmp = p // speed + flag
            t += tmp

        return t <= H


# Piles = [3, 6, 7, 11]
Piles = [30, 11, 23, 4, 20]
h = 5
print(Solution().minEatingSpeed(Piles, h))
