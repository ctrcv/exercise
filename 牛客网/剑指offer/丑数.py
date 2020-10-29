# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here

        # 1. 自写， 回溯，超时， 复杂度高
        # res = set()
        # res.add(1)
        # nums = [2, 3, 5]
        #
        # def backtrack(x, n):
        #     if x == 1 or x in res:
        #         # res.append(n)
        #         res.add(n)
        #         return
        #
        #     for num in nums:
        #         if x % num == 0:
        #             x = x / num
        #             backtrack(x, n)
        #             x = x * num
        #
        # m = 2
        # while len(res) < index:
        #     backtrack(m, m)
        #     m += 1
        # return sorted(list(res))[index - 1]

        # 2. 剑指offer中的示例解法1，复杂度高， 超时

        # def isUgly(num):
        #     while num % 2 == 0:
        #         num /= 2
        #     while num % 3 == 0:
        #         num /= 3
        #     while num % 5 == 0:
        #         num /= 5
        #
        #     return num == 1
        #
        # if index <= 0:
        #     return 0
        #
        # number = 0
        # cnt = 0
        # while cnt < index:
        #     number += 1
        #     if isUgly(number):
        #         cnt += 1
        # return number

        # 3. 剑指offer示例解法
        if index <= 0:
            return 0

        ugly_numbers = [1] * index
        # 三个索引
        a, b, c = 0, 0, 0
        cnt = 1
        while cnt < index:
            # 将已有的丑数分别乘以2，3，5， 最小的数为下一个丑数
            multi2, multi3, multi5 = ugly_numbers[a] * 2, ugly_numbers[b] * 3, ugly_numbers[c] * 5
            ugly_numbers[cnt] = min(multi2, multi3, multi5)

            if ugly_numbers[cnt] == multi2:
                a += 1
            if ugly_numbers[cnt] == multi3:
                b += 1
            if ugly_numbers[cnt] == multi5:
                c += 1

            cnt += 1
        print(ugly_numbers)
        return ugly_numbers[- 1]

        # 参考：https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/
        # dp, a, b, c = [1] * index, 0, 0, 0
        # for i in range(1, index):
        #     n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        #     dp[i] = min(n2, n3, n5)
        #     if dp[i] == n2: a += 1
        #     if dp[i] == n3: b += 1
        #     if dp[i] == n5: c += 1
        # return dp[-1]


ans = Solution().GetUglyNumber_Solution(20)
print(ans)
