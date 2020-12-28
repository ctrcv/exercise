from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_edge = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    # [i,j] 位置的正方形大小取决于左上角的可形成的最大正方形的最小值
                    # 即取三者中的最小值+1
                    # 如下例中，可形成的最大正方形面积为16而不是25
                    #           [["1", "1", "1", "1", "0"],
                    #           ["1", "1", "1", "1", "0"],
                    #           ["1", "1", "1", "1", "1"],
                    #           ["1", "1", "1", "1", "1"],
                    #           ["0", "0", "1", "1", "1"]]
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

                max_edge = max(dp[i][j], max_edge)

        return max_edge * max_edge


# Matrix = [
#     ["1","0","1","0","0"],
#     ["1","0","1","1","1"],
#     ["1","1","1","1","1"],
#     ["1","0","0","1","0"]
# ]

# Matrix = [["0","1"],["1","0"]]
# Matrix = [["0"]]
# 情况4
# Matrix = [["1", "1", "1", "1", "0"],
#           ["1", "1", "1", "1", "0"],
#           ["1", "1", "1", "1", "1"],
#           ["1", "1", "1", "1", "1"],
#           ["0", "0", "1", "1", "1"]]

print(Solution().maximalSquare(Matrix))
