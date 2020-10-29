# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a, b = 1, 1
        for _ in range(number):
            a, b = b, a + b

        return a


m = 7
print(Solution().jumpFloor(m))
