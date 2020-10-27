class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 参考LCS的思路
        m, n = len(word1), len(word2)
        # 状态dp[i][j]表示最少的操作数使得word1的前i个字符和word2的前j个字符
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): dp[i][0] = i  # word2 为空，需要的最少步数，就是删除操作
        for j in range(n + 1): dp[0][j] = j  # word1 为空变成 word2 最少步数，就是插入操作

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 当元素相同时，不进行操作
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 否则，对比
                else:
                    # dp[i - 1][j-1]可以理解为替换操作，dp[i][j-1]为插入，dp[i-1][j]为删除？？
                    # 对“dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。”的补充理解：
                    #
                    # 以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，即要将 word1的前 5 个字符转换为 word2的前 3 个字符，
                    # 也就是将 horse 转换为 ros，因此有：
                    #
                    # (1) dp[i-1][j-1]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 2 个字符 ro，然后将第五个字符 word1[4]（
                    # 因为下标基数以 0 开始） 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）
                    #
                    # (2) dp[i][j-1]，即先将 word1 的前 5 个字符 horse 转换为 word2 的前 2 个字符 ro，然后在末尾补充一个 s，即插入操作
                    #
                    # (3) dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，然后删除 word1 的第 5 个字符
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, min(dp[i][j - 1] + 1, dp[i - 1][j] + 1))

        return dp[m][n]


Word1 = 'intention'
Word2 = 'execution'
print(Solution().minDistance(Word1, Word2))
