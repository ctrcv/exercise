class Solution:
    # 1.暴力解法
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) < 2:
    #         return s
    #     left = right = 0
    #     maxlen = 1
    #     n = len(s)
    #     for i in range(n):
    #         for j in range(n - 1, i, -1):
    #             if s[i] == s[j] and self._valid(s, i, j):
    #                 if j - i + 1 > maxlen:
    #                     left, right = i, j
    #                     maxlen = j - i + 1
    #
    #     return s[left: right + 1]
    #
    # def _valid(self, s, i, j):
    #     while i < j:
    #         if s[i] != s[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True

    # 2.动态规划解法, O(N^2), O(N^2)
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if n < 2:
    #         return s
    #     maxlen = 0
    #     left = right = 0
    #     dp = [[False] * n for _ in range(n)]
    #     # for i in range(n):
    #     #     dp[i][i] = True
    #
    #     # 注意表格填写顺序
    #     for j in range(1, n):
    #         for i in range(j - 1, -1, -1):
    #             if s[i] == s[j]:
    #                 if j - i < 3:
    #                     # 考虑dp[i+1][j-1]的边界情况
    #                     # 即[i+1, j-1]不构成区间，即长度严格小于2
    #                     # 即j - 1 - (i + 1) + 1 < 2
    #                     dp[i][j] = True
    #                 else:
    #                     dp[i][j] = dp[i + 1][j - 1]
    #             else:
    #                 dp[i][j] = False
    #
    #             if dp[i][j]:
    #                 curlen = j - i + 1
    #                 if curlen > maxlen:
    #                     left, right = i, j
    #                     maxlen = curlen
    #
    #     return s[left: right + 1]

    # 3.中心扩散， O(N^2), O(1),比动态规划耗时更少
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if len(s) < 2:
            return s

        maxlen = 1
        res = s[0]
        for i in range(n):
            # 分奇数和偶数的情况
            odd, odd_len = self._center_spread(s, n, i, i)
            even, even_len = self._center_spread(s, n, i, i + 1)

            cur_max_substr = odd if odd_len > even_len else even
            cur_len = len(cur_max_substr)
            if cur_len > maxlen:
                maxlen = cur_len
                res = cur_max_substr

        return res

    def _center_spread(self, s, n, i, j):
        left, right = i, j
        while left > 0 and j < n and s[i] == s[j]:
            left -= 1
            right += 1

        return s[left + 1: right], right - left + 1


# S = 'babad'
S = 'dddd'
# S = 'cbbd'
# S = 'ccc'
# S = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

print(Solution().longestPalindrome(S))
