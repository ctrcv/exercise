class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. 暴力匹配:O(N^3), O(1)
        # n = len(s)
        # if n < 2:
        #     return s
        #
        # maxlen = 1
        # res = s[0]
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if self.isPalindrome(s, i, j) and j - i + 1 > maxlen:
        #             maxlen = j - i + 1
        #             res = s[i: j + 1]
        #
        # return res

        # def isPalindrome(self, s, left, right):
        #     while left < right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #
        #     return True

        # 2.动态规划：O(N^2), O(N^2)
        # n = len(s)
        # if n < 2:
        #     return s
        # # dp[i][j]状态表示从索引i到j的子串是否为回文
        # dp = [[False] * n for _ in range(n)]
        # start, maxlen = 0, 1
        # for i in range(n):
        #     dp[i][i] = True
        #
        # 注意填表顺序
        # for j in range(1, n):
        #     for i in range(0, n):
        #         if s[i] == s[j]:
        #             if j - 1 - (i + 1) + 1 < 2:
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = dp[i + 1][j - 1]
        #         else:
        #             dp[i][j] = False
        #
        #         if dp[i][j]:
        #             cur_len = j - i + 1
        #             if cur_len > maxlen:
        #                 maxlen = cur_len
        #                 start = i
        #         return s[start:start + maxlen]

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxlen = 1
        res = s[0]
        for i in range(n):
            dp[i][i] = True

        for j in range(1, n):
            for i in range(n):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    res = s[i: i + maxlen]

        return res






        # 3. 中心扩撒法
    #     size = len(s)
    #     if size < 2:
    #         return s
    #
    #     # 至少是 1
    #     max_len = 1
    #     res = s[0]
    #
    #     for i in range(size):
    #         palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
    #         palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)
    #
    #         # 当前找到的最长回文子串
    #         cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
    #         if len(cur_max_sub) > max_len:
    #             max_len = len(cur_max_sub)
    #             res = cur_max_sub
    #
    #     return res
    #
    # def __center_spread(self, s, size, left, right):
    #     """
    #     left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
    #     right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
    #     """
    #     i = left
    #     j = right
    #
    #     while i >= 0 and j < size and s[i] == s[j]:
    #         i -= 1
    #         j += 1
    #     return s[i + 1:j], j - i - 1


S = "aba"
print(Solution().longestPalindrome(S))
