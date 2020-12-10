from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            dic[n] = i

        # for i, n in enumerate(nums):
        #     dif = target - n
        #     if dif in dic and dic[dif] != i:
        #         res.append(i)
        #         res.append(dic[dif])
        #         break
        #
        # return res
        for i, n in enumerate(nums):
            dif = target - n
            if dif in dic and dic[dif] != i:
                return [i, dic[dif]]

# Nums = [4, 3, 4, -4]
# T = 8
# Nums = [2, 7, 11, 15]
# T = 9
Nums = [3, 2, 4]
T = 6
print(Solution().twoSum(Nums, T))
