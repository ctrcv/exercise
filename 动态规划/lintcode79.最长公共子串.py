class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """

    # 1.暴力解法
    # def longestCommonSubstring(self, A, B):
    #     # write your code here
    #     m, n = len(A), len(B)
    #     maxlen = 0
    #
    #     for i in range(m):
    #         k = i
    #         for j in range(n):
    #             cnt = 0
    #             # if A[i: i + 3] == 'dnf' and B[j: j + 2] == 'dn':
    #             while i < m and j < n and A[i] == B[j]:
    #                 i += 1
    #                 j += 1
    #                 cnt += 1
    #             i = k
    #             maxlen = max(maxlen, cnt)
    #
    #     return maxlen

    # 2. 动态规划
    def longestCommonSubstring(self, A, B):
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxlen = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0

                maxlen = max(dp[i][j], maxlen)
        return maxlen


# s1 = "ABCD"
# s2 = "CBCE"
# s1, s2 = "ABCD", "EACB"
s1, s2 = "adfanadsnf;andvadsjfafjdlsfnaldjfi*odiasjfasdlnfasldgao;inadfjnals;dfjasdl;jfa;dsjfa;sdnfsd;afhwery894yra7f78asfas8fy43rhaisuey34hiuy^%(9afysdfhaksdhfsdkjfhsdhfakldhfsdkf*h", "dafdnf**"
print(Solution().longestCommonSubstring(s1, s2))
