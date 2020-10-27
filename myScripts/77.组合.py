class Solution(object):
    # 自写：回溯
    # def combine(self, n, k):
    #     ans = []
    #     visited = set()
    #
    #     def dfs(res, val):
    #         if len(res) == k:
    #             ans.append(res[:])
    #             return
    #
    #         for num in range(1, n + 1):
    #             res.append(num)
    #             if val not in visited:
    #                 visited.add(num)
    #                 dfs(res, num)
    #             res.pop()
    #             visited.discard(num)
    #
    #     dfs([], 0)
    #     print(ans)
    #     return ans

    def combine(self, n, k):
        ans = []
        # tmp = []
        def dfs(tmp, curr):
            # 剪枝：temp 长度加上区间 [cur, n] 的长度小于 k，不可能构造出长度为 k 的 temp
            if len(tmp) + (n - curr + 1) < k:
                return
            # 记录合法的答案
            if len(tmp) == k:
                ans.append(tmp[:])
                return
            # curr == n + 1 的时候结束递归
            if curr == n + 1:
                return

            # 考虑选择当前位置
            tmp.append(curr)
            # print('递归前： ', tmp)
            dfs(tmp, curr + 1)
            # print('递归后: ', tmp)
            tmp.pop()
            # 考虑不选择当前位置
            dfs(tmp, curr + 1)

        dfs([], 1)
        # print(ans)
        return ans


Solution().combine(4, 3)

