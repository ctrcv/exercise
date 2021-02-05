# # 异或
# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         res = 0
#         t = x ^ y
#         while t:
#             t &= (t - 1)
#             # 每经过一次t &= t - 1，都会消除t对应的二进制的最右边的“1”
#             res += 1
#
#         return res


# 使用移位的方式，检查最右侧或最左侧的元素是否为1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0
        while xor:
            if xor & 1:
                res += 1
            xor >>= 1
        return res


a, b = 1, 2
print(Solution().hammingDistance(a, b))
