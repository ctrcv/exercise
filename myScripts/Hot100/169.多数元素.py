from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1.哈希表计数
        # 2.排序
        # 3. 摩尔投票法：从第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换个数开始计数，总能找到最多的那个
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if res == nums[i]:
                count += 1
            elif count == 0:
                res = nums[i]
                count = 1
            else:
                count -= 1
        return res

# Nums = [3,2,3]
Nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(Nums))