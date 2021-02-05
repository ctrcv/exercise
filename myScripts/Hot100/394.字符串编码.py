class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return ""

        # 方法1：辅助栈，时间空间复杂度均为O(N)
        stack, res, multi = [], "", 0
        # 从左往右遍历
        for c in s:
            # 当c等于[时，将乘数multi和字符串压入栈中，并随后置空置零
            if c == "[":
                stack.append((multi, res))
                res, multi = "", 0
            # 当c等于]时，将栈顶元素弹出
            elif c == "]":
                curr_multi, last_res = stack.pop()
                res = last_res + curr_multi * res
            # 数字
            elif c.isdigit():
                multi = int(c) + multi * 10
            # 字母
            else:
                res += c

        return res


# class Solution:
#     def decodeString(self, s: str) -> str:
#         if not s: return ""
#
#         # 方法2：递归法,时间空间复杂度均为O(N)
#         def dfs(s, i):
#             res, multi = "", 0
#             while i < len(s):
#                 if s[i].isdigit():
#                     multi = int(s[i]) + multi * 10
#                 elif s[i] == "[":
#                     # 当 s[i] == '[' 时，开启新一层递归，记录此 [...] 内字符串 tmp 和递归后的最新索引 i，
#                     # 并执行 res + multi * tmp 拼接字符串。
#                     i, tmp = dfs(s, i + 1)
#                     res += multi * tmp
#                     multi = 0
#                 elif s[i] == "]":
#                     # 当 s[i] == ']' 时，返回当前括号内记录的 res 字符串与 ] 的索引 i （更新上层递归指针位置）；
#                     return i, res
#                 else:
#                     res += s[i]
#                 i += 1
#             return res
#
#         return dfs(s, 0)


# S = "3[a]2[bc]"  # aaabcbc
# S = "3[a2[c]]"  # accaccacc
# S = "2[abc]3[cd]ef"  # abcabccdcdcdef
# S = "abc3[cd]xyz"  # abccdcdcdxyz
S = "100[leetcode]"  # abccdcdcdxyz
print(Solution().decodeString(S))
