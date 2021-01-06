from typing import List
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         # 方法1:通过单独的位1计数函数,时间复杂度为O(nk),k为整数的位数
#         ans = []
#         for i in range(num + 1):
#             ans.append(self.popcount(i))
#         return ans
#
#     def popcount(self, x):
#         """
#         位1的个数方法
#         """
#         # 方法1和方法2的时间复杂度均为O(k),其中k为整数x的位数;空间复杂度O(1)
#         # 方法1:循环和位移动
#         # 使用位掩码的方式,统计1的个数.
#         # 整型数字通常为32位
#
#         # bits = 0
#         # mask = 1
#         # for i in range(32):
#         #     if x & mask != 0:
#         #         bits += 1
#         #     mask <<= 1
#         #
#         # return bits
#
#         # 方法2:
#         # 位操作小技巧
#         # 在二进制表示中，数字n中最低位的1总是对应 n−1 中的0。
#         # 因此，将n和n - 1与运算总是能把n中最低位的 1变成0，并保持其他位不变
#         bits = 0
#         while x != 0:
#             bits += 1
#             x &= x - 1
#
#         return bits

class Solution:
    def countBits(self, num: int) -> List[int]:
        # 方法2:动态规划 + 最后设置位
        # 使用x &= x - 1将该位设置为0,则状态转移函数为:
        # p(x) = p(x & (x - 1)) + 1
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans


Num = 5
print(Solution().countBits(Num))