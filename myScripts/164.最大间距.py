from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        ans = 0
        for i in range(1, n):
            dis = nums[i] - nums[i - 1]
            ans = max(dis, ans)

        return ans


Nums = [3,6,9,1]
print(Solution().maximumGap(Nums))
