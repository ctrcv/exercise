from typing import List


# 超时
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         if not s or not p:
#             return []
#         ns, np = len(s), len(p)
#         res = []
#         hashp = {}
#         for i in range(np):
#             ch = p[i]
#             hashp[ch] = hashp.get(ch, 0) + 1
#
#         for i in range(ns - np + 1):
#             hashs = {}
#             for j in range(np):
#                 ch = s[i + j]
#                 hashs[ch] = hashs.get(ch, 0) + 1
#             if hashs == hashp:
#                 res.append(i)
#
#         return res

# 滑动窗口
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        ns, np = len(s), len(p)
        left, right = 0, np

        window = {}
        while right < ns:
            ch = s[left]
            window[ch] = window.get(ch, 0) + 1


# S = "cbaebabacd"
# P = "abc"
S = "abab"
P = "ab"
print(Solution().findAnagrams(S, P))
