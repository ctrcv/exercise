class Solution:
    def findItinerary(self, tickets):

        # 方法1： DFS
        # import collections
        # d = collections.defaultdict(list)  # 邻接表
        # for f, t in tickets:
        #     d[f] += [t]  # 路径存进邻接表
        #
        # for f in d:
        #     d[f].sort()  # 邻接表排序
        #
        # ans = []
        #
        # def dfs(f):  # 深搜函数
        #     while d[f]:
        #         dfs(d[f].pop(0))  # 路径检索
        #     ans.insert(0, f)  # 放在最前
        #
        # dfs('JFK')
        # return ans

        # 方法2：回溯法  拉不拉东回溯框架
        from collections import defaultdict
        tickets_dict = defaultdict(list)
        for t in tickets:
            tickets_dict[t[0]].append(t[1])

        path = ['JFK']

        def backtrack(curr_from):
            # 结束条件
            if len(path) == len(tickets) + 1:
                return True

            # 对子路径排序
            tickets_dict[curr_from].sort()
            for t in tickets_dict[curr_from]:
                curr_to = tickets_dict[curr_from].pop(0)  # 删除当前节点
                path.append(curr_to)  # 做选择
                if backtrack(curr_to):  # 进入下一个决策层
                    return True
                path.pop()  # 撤销选择
                tickets_dict[curr_from].append(curr_to)  # 恢复当前节点

            return False

        backtrack('JFK')
        return path


tics = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
s = Solution().findItinerary(tics)
print(s)
