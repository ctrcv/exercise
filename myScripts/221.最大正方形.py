from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        # 1. 暴力
        # 以当前点为左上角啊，向后计算最大的正方形大小

        # maxval = 0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == '1':
        #             maxval = max(maxval, 1)
        #
        #             cur_side = min(m - i, n - j)
        #
        #             for p in range(1, cur_side):
        #                 flag = True
        #                 if matrix[i + p][j + p] == '0':
        #                     break
        #                 for q in range(0, p):
        #                     if matrix[i + p][j + q] == '0' or matrix[i + q][j + p] == '0':
        #                         flag = False
        #                         break
        #                 if flag:
        #                     maxval = max(maxval, p + 1)
        #                 else:
        #                     break
        #
        # return maxval * maxval

        # 2.dp
        # 参考：https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode-solution/
        dp = [[0] * n for _ in range(m)]
        maxval = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    # 转移方程推导参考：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/tong-ji-quan-wei-1-de-zheng-fang-xing-zi-ju-zhen-2/
                    maxval = max(dp[i][j], maxval)

        return maxval * maxval


arr = [['1', '0', '1', '0', '0'],
       ['1', '0', '1', '1', '1'],
       ['1', '1', '1', '1', '1'],
       ['1', '0', '0', '1', '0']]

print(Solution().maximalSquare(arr))
