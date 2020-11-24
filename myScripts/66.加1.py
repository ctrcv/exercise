from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        def dfs(i):
            t = digits[i] + 1
            if t >= 10:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    return
                digits[i] = 0
                dfs(i - 1)
            else:
                digits[i] = t

        dfs(n - 1)
        return digits


dig = [9, 9, 9]
# dig = [1,2,3]
print(Solution().plusOne(dig))
