# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return
        n = len(numbers)
        arr = [0] * n
        for num in numbers:
            arr[num - 1] += 1

        for i, a in enumerate(arr):
            if a > n // 2:
                return i + 1

        return 0


nums = [1, 2, 2, 3, 3, 2, 3, 3, 2]
print(Solution().MoreThanHalfNum_Solution(nums))
