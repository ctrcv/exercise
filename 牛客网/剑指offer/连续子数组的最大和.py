# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        # 原代码
        # dp = [0] * n
        # for i in range(n):
        #     if i == 0:
        #         dp[0] = array[i]
        # #
        #     # elif dp[i - 1] > 0:
        #     #     dp[i] = dp[i - 1] + array[i]
        #     # else:
        #     #     dp[i] = array[i]
        #
        #     dp[i] = max(dp[i-1] + array[i], array[i])
        # return max(dp)

        #  修改1
        # dp = [0] * n
        # ret = 0
        # for i in range(n):
        #     if i == 0:
        #         dp[0] = array[i]
        #         ret = array[i]
        #     dp[i] = max(dp[i - 1] + array[i], array[i])
        #     ret = max(ret, dp[i])
        # return ret

        # 修改2
        # a, b = 0, 0
        # ret = 0
        # for i in range(n):
        #     if i == 0:
        #         a = array[i]
        #         ret = array[i]
        #         continue
        #     b = max(a + array[i], array[i])
        #     ret = max(ret, b)
        #     a = b
        #
        # return ret

        # 修改3
        # 初始化：维护一个变量tmp = 0
        # 如果tmp+array[i] < 0, 说明以i结尾的不作贡献，重新赋值tmp = 0
        # 否则更新tmp = tmp + array[i]
        # 最后判断tmp是否等于0， 如果等于0， 说明数组都是负数，选取一个最大值为答案。
        ret = array[0]
        tmp = 0
        for k in array:
            if tmp + k < 0:
                tmp = 0
            else:
                tmp = tmp + k
            ret = max(tmp, ret)
        if tmp != 0:
            return ret

        return max(array)


nums = [6, -3, -2, 7, -15, 1, 2, 2]  # 8
# nums = [-2, -8, -1, -5, -9]  # -1
print(Solution().FindGreatestSumOfSubArray(nums))
