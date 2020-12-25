from typing import List

# 深度优先搜索，时间空间复杂度均为O(MN)
# 扫描整个二维网格。如果一个位置为 1，则以其为起始节点开始进行深度优先搜索。
# 在深度优先搜索的过程中，每个搜索到的 11 都会被重新标记为 0。
# 最终岛屿的数量就是行深度优先搜索的次数

# class Solution:
#     def _dfs(self, grid, i, j):
#         # 将网格中该位置的元素置0，表示该点已遍历过
#         grid[i][j] = 0
#         m, n = len(grid), len(grid[0])
#         directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#         for dx, dy in directions:
#             x, y = i + dx, j + dy
#             # 如果没有越界，且该点等于"1"，则继续进行搜索
#             if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
#                 self._dfs(grid, x, y)
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         m, n = len(grid), len(grid[0])
#         nums = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     self._dfs(grid, i, j)
#                     nums += 1
#         return nums


import collections
# 广度优先搜索，时间复杂度O(MN), O(min(M,N))
# 扫描整个二维网格。如果一个位置为 11，则将其加入队列，开始进行广度优先搜索。
# 在广度优先搜索的过程中，每个搜索到的 11 都会被重新标记为 00。直到队列为空，搜索结束。
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands


Grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# Grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
print(Solution().numIslands(Grid))
