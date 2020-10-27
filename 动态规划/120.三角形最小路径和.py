from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0

        # dp = [[] for _ in range(len(triangle))]
        # for i in range(len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if i == 0 and j == 0:
        #             dp[i].append(triangle[i][j])
        #         elif j == 0 and i > 0:
        #             dp[i].append(dp[i - 1][j] + triangle[i][j])
        #         elif j == len(triangle[i]) - 1 and i > 0:
        #             dp[i].append(dp[i - 1][j - 1] + triangle[i][j])
        #         else:
        #             # print(i, j)
        #             tmp = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        #             dp[i].append(tmp)
        #
        # # print(dp)
        # return min(dp[-1])

        # 使用滚动数组优化空间复杂度
        n = len(triangle)
        ans = 1e10
        dp = [0] * (n + 1)
        for i in range(n):
            for j in range(len(triangle[i]) - 1, -1, -1):
                if j == len(triangle[i]) - 1:
                    dp[j + 1] = triangle[i][j] + dp[j]
                elif j == 0:
                    dp[j + 1] = triangle[i][j] + dp[j + 1]
                else:
                    dp[j + 1] = triangle[i][j] + min(dp[j + 1], dp[j])

                if i == n - 1:
                    ans = min(ans, dp[j + 1])

        return ans


arr = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print(Solution().minimumTotal(arr))
