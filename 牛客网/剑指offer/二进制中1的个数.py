# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 参考的解析：https://blog.nowcoder.net/n/66731e3de0d94e35adeeda43c3fec888?f=comment
        count = 0
        if n < 0:
            # 如果是数字，需要将其转换成补码形式
            n = n & 0xffffffff

        while n:
            count += 1
            n = n & (n - 1)

        return count


print(Solution().NumberOf1(-3))