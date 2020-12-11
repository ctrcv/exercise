from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. 暴力法：超时
        # n = len(height)
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         t = (j - i) * min(height[i], height[j])
        #         res = max(res, t)
        #
        # return res

        # 2.双指针
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            t = (j - i) * min(height[i], height[j])
            res = max(res, t)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return res


H = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# H = [1, 2, 1]
print(Solution().maxArea(H))
