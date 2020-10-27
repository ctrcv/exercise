# 题目描述
# 放苹果：把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
# 整数拆分

# f[m][n] 表示m个苹果分到n个盘中
# 1. 当盘数n大于m的时候，空出的盘对结果无影响
# 2. 当盘数n <= m 时， （1）有x个盘是空的，m个苹果全部放在n-x个盘中; (2) 每个盘至少放一个苹果
# 因此，综合2的情况，f[m][n] = f[m][n-1] + f[m - n][n]


class Solution:
    # 递归形式
    # https://www.cnblogs.com/2016024291-/p/6686261.html
    def func(self, m, n):
        if m == 0 or n == 1:
            return 1
        if n > m:
            return self.func(m, m)
        else:
            return self.func(m, n - 1) + self.func(m - n, n)

    # 动态规划形式
    # 参考：https://blog.csdn.net/zmingyang/article/details/107057978?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
    # http://blog.chinaunix.net/uid-26548237-id-3503956.html
    def func2(self, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 1 or j == 1:
                    dp[i][j] = 1
                elif i == j:
                    dp[i][j] = 1 + dp[i][j - 1]
                elif i < j:
                    dp[i][j] = dp[i][i]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - j][j]

        return dp[m][n]


print(Solution().func(5, 5))
print(Solution().func2(5, 5))
