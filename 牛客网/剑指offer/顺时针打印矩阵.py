# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix is None:
            return
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [v[0] for v in matrix]
        m, n = len(matrix), len(matrix[0])

        sz = m * n
        ans = []
        cnt = 0
        i, j = 0, 0
        while cnt != sz:
            left_right = matrix[i][j: n]
            ans.extend(left_right)  # 左到右
            cnt += len(left_right)

            up_down = [matrix[t][n - 1] for t in range(i + 1, m)]
            ans.extend(up_down)  # 上到下
            cnt += len(up_down)

            right_left = [matrix[m - 1][t] for t in range(n - 2, j - 1, -1)]
            ans.extend(right_left)  # 右到左
            cnt += len(right_left)

            down_up = [matrix[t][j] for t in range(m - 2, i, -1)]
            ans.extend(down_up)  # 下到上
            cnt += len(down_up)

            if i < m:
                i += 1
            if j < n:
                j += 1
            m -= 1
            n -= 1
            print(ans)
        return ans


# nums = [[1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]]
# nums = [[1], [2], [3], [4], [5], [6]]
# nums = [[1, 2, 3, 4, 5, 6]]
nums = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]]
print(Solution().printMatrix(nums))
