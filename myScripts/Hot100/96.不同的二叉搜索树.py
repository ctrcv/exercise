class Solution:
    def numTrees(self, n: int) -> int:
        # 动态规划方法
        # 思想：假设n个节点存在二叉搜索树的个数是G(n)，令f(i)表示以i为根节点的二叉搜索树的个数，则：
        # G(n) = f(1) + f(2) + ... + f(n)
        # 当i为根节点时，左子树节点个数为 i-1 个，右子树节点个数为 n-i，则
        # f(i) = G(i - 1) * G(n - i)
        # 综上，G(n) = G(0) * G(n-1) + G(1) * G(n - 2) + ... + G(n - 1) * G(0)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]


N = 3
print(Solution().numTrees(N))