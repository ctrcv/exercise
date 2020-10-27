from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        cnt = 1
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

        return ans


arr = [1,3,5,4,7]
print(Solution().findLengthOfLCIS(arr))

