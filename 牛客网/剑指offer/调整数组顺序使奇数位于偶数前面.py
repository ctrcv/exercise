# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return []

        ans = []
        for a in array:
            if a & 1:
                ans.append(a)
        for a in array:
            if a % 2 == 0:
                ans.append(a)

        return ans


nums = [2, 8, 2, 1, 3, 3, 5]
print(Solution().reOrderArray(nums))
