from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心思想，尽可能到达最远的位置
        # 主要思想：如果能到达某个位置，那一定能到达它前面的所有位置
        # 方法：初始化最远位置为 0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。
        # 初始化当前能够到达的最远位置
        # max_i = 0
        # for i in range(len(nums)):
        #     # 如果当前位置可达，且当前位置加上当前位置能够跳跃的最大跳数大于最远跳数
        #     # 则更新最远跳数max_i
        #     if max_i >= i:
        #         max_i = max(max_i, i + nums[i])
        #
        # # 如果最远跳数大于数组长度，则表示能够到达最后的位置
        # return max_i >= len(nums)

        # 小简化，提升速度
        max_i = 0
        for i in range(len(nums)):
            # 如果位置i大于能够到达的最远跳数，则说明当前位置之前的最大跳数不能够达到当前位置，说明后面位置也永远到达不了，直接返回
            if i > max_i: return False
            max_i = max(max_i, i + nums[i])
        return True


Nums = [2, 3, 1, 1, 4]
print(Solution().canJump(Nums))
