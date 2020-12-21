class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 方法1：深度搜索DFS，运行超时
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

        # 方法2：动态规划，时间复杂度O(MN),空间O(MN)
        # 主要思想：能够到达当前位置的路径和等于能够到达上一行同列位置的路径数 + 同一行前一列的路径数之和
        # dp = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         # 由于只能向下向右移动，所以第一行和第一列的位置能到达的路径数为1
        #         if i == 0 or j == 0:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        #
        # return dp[-1][-1]

        # 方法3：动态规划，空间优化，时间复杂度O（MN）， 空间复杂度O（2N）= O(N)
        # 优化依据：dp[i][j]每次只与dp[i-1][j] 和 dp[i][j-1]有关
        # pre: 前一行，curr：当前行
        # pre, curr = [1] * n, [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         curr[j] = pre[j] + curr[j - 1]
        #     pre = curr
        # return curr[-1]

        # 方法4：动态优化，空间优化,O(N)
        # 优化依据：?
        curr = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                curr[j] += curr[j - 1]
        return curr[-1]


M, N = 3, 7
# M, N = 3, 3
print(Solution().uniquePaths(M, N))
