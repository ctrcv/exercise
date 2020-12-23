from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 使用set进行去重和降低查询复杂度
        # 时间复杂度和空间复杂度：O(n)
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            # 因为num-1在while循环中已经遍历过了，不需要重复遍历
            if num - 1 not in num_set:
                curr_num = num
                curr_len = 1
                # 如果有连续的数字，则一直遍历下去
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len


# Nums = [100, 4, 200, 1, 3, 2]
Nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(Nums))
