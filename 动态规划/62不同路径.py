class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. 深度搜索, 超时
        # visited = [[False] * n for _ in range(m)]
        # global res
        # res = 0
        #
        # def dfs(i, j):
        #     if i == m - 1 and j == n - 1:
        #         global res
        #         res += 1
        #         return
        #
        #     if i < m and j < n:
        #         if not visited[i][j]:
        #             visited[i][j] = True
        #             dfs(i + 1, j)
        #             dfs(i, j + 1)
        #             visited[i][j] = False
        #
        # dfs(0, 0)
        # return res

        # 2. 动态规划
        # dp = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        #
        # return dp[-1][-1]

        # 3. 动态规划空间优化1：O(2n)
        # pre = [1] * n
        # curr = [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         curr[j] = pre[j] + curr[j - 1]
        #     pre = curr[:]
        # return pre[-1]

        # 4. 动态规划空间复杂度2：O（n）
        curr = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                curr[j] += curr[j - 1]

        return curr[-1]


ans = Solution().uniquePaths(3, 7)
print(ans)
