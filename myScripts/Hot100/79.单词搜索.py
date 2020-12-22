from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 方法：回溯法。
        # 时间复杂度：宽松上界：O(MN*3^L)，L表示word的长度
        # 在每次调用函数  时，除了第一次可以进入4个分支以外，
        # 其余时间我们最多会进入3个分支（因为每个位置只能使用一次，所以走过来的分支没法走回去）。
        # 由于单词长为 L，故 dfs(i, j, 0) 的时间复杂度为 O(3^L),而我们要执行 O(MN)次检查
        # 空间复杂度：O(MN)。额外开辟了used数组，同时栈的最大深度为O(min(L, MN))

        m, n = len(board), len(board[0])
        used = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, k):
            # 如果borad[i][j] 与word的第k个字符不相同，则表示匹配错误
            if board[i][j] != word[k]:
                return False
            # 如果字符匹配，且已经访问到结尾，则搜索成功
            if k == len(word) - 1:
                return True

            # 标记该点已经遍历过
            used[i][j] = True
            for di, dj in directions:
                # 对四个方向遍历
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n:
                    if not used[newi][newj]:
                        # 因为当前已经匹配了word的地k个字符，所以下一个匹配的字符是第word的k+1位的字符
                        if dfs(newi, newj, k + 1):
                            return True
            # 回溯
            used[i][j] = False

        # ！！！注意：因为可以从board上的任意位置开始搜索，所以需要遍历每个位置
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


Board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]
# Word = "ABCCED"
# Word = "SEE"
Word = "ABCB"
print(Solution().exist(Board, Word))
# Solution().exist(Board, Word)
