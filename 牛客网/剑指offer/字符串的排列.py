# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here

        # 1. 回溯
        # if not ss:
        #     return []
        #
        # n = len(ss)
        # visited = [False] * n
        # res = set()
        #
        # def dfs(path):
        #     if len(path) == n:
        #         res.add(''.join(path))
        #         return
        #
        #     for i in range(n):
        #         if not visited[i]:
        #             visited[i] = True
        #             path.append(ss[i])
        #             dfs(path)
        #             visited[i] = False
        #             path.pop()
        #
        # dfs([])
        # return sorted(list(res))

        # 2. 回溯_交换位置
        # 参考：https://blog.nowcoder.net/n/cd2ff5b6b5a541358debc59ada0110b8?f=comment
        if not ss:
            return []
        res = set()

        def perm(pos, s):
            if pos + 1 == len(s):
                res.add(''.join(s))
                return

            for i in range(pos, len(ss)):
                s[pos], s[i] = s[i], s[pos]
                perm(pos + 1, s)
                s[pos], s[i] = s[i], s[pos]

        perm(0, list(ss))
        return sorted(list(res))


chars = "abc"
# chars = "aab"
print(Solution().Permutation(chars))
