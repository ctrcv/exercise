class Solution(object):
    # 栈方法
    # 时间：O（M+N）
    # 空间：O（M+N）
    # def backspaceCompare(self, S: str, T: str) -> bool:
    #     S1 = self._helper(S)
    #     T1 = self._helper(T)
    #     return S1 == T1
    #
    # def _helper(self, s):
    #     res = []
    #     for i in range(len(s)):
    #         if s[i] == '#':
    #             if res:
    #                 res.pop()
    #         else:
    #             res.append(s[i])
    #
    #     # 提交记录对比发现使用join函数后的速度和空间均比直接返回list对比更好
    #     # join：时间28ms，空间13.4M
    #     # list：时间32ms，空间13.4
    #     return ''.join(res)

    # 双指针: 逆序遍历
    # 时间： O（M + N）
    # 空间： O（1）
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if T[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1
        return True


s = 'ab#c'
t = 'ab#c'
print(Solution().backspaceCompare(s, t))
