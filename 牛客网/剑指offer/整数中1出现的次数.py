# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        def count(x):
            # if x <= 13:
            #     return 6
            cnt = 0
            while x:
                k = x % 10
                x //= 10
                if k == 1:
                    cnt += 1

            return cnt

        ret = 0
        for i in range(1, n + 1):
            ret += count(i)

        return ret


N = 15
print(Solution().NumberOf1Between1AndN_Solution(N))