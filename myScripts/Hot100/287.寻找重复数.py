from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            a = nums[i] ^ a
        return a


Nums = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(Nums))
