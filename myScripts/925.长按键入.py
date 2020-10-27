class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        m, n = len(name), len(typed)
        while j < n:
            # 如果相等， 双指针右移
            if i < m and name[i] == typed[j]:
                i += 1
                j += 1
            # 判断是否是因为长按导致的
            elif j > 0 and typed[i] == typed[i - 1]:
                j += 1
            # 都不满足，则直接返回
            else:
                return False
        # 最后判断name中的字符是否全部匹配
        return i == m


# False
# Name = 'xnhtq'
# Typed = "xhhttqq"
# True
# Name = "alex"
# Typed = "aaleex"
# False
# Name = "saeed"
# Typed = "ssaaedd"
# False
Name = "kikcxmvzi"
Typed = "kiikcxxmmvvzz"
print(Solution().isLongPressedName(Name, Typed))
