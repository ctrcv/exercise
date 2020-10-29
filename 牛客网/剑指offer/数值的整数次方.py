# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here

        # 方法1：分解递归
        # if exponent == 0:
        #     return 1
        # if base == 0:
        #     return 0
        # if base == 1:
        #     return 1
        # if exponent < 0:
        #     base = 1 / base
        #     exponent *= -1
        #
        # res = self.Power(base, exponent // 2)
        # res = res * res
        # if exponent % 2 != 0:
        #     res *= base
        #
        # return res

        # 方法2：
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        if base == 1:
            return 1
        if exponent < 0:
            base = 1 / base
            exponent *= -1

        res = 1
        while exponent:
            if exponent & 1:
                res *= base

            base *= base
            exponent >>= 1
        return res


print(Solution().Power(2, 5))
