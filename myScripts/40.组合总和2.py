from typing import List
class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        ans = []
        candidates = sorted(candidates)
        n = len(candidates)


        # 自写
        # def backtrack(s, t, cand):
        #     if t < 0:
        #         return
        #     if t == 0:
        #         if s not in ans:
        #             ans.append(s[:])
        #         return
        #
        #     for i, item in enumerate(cand):
        #         s.append(item)
        #         backtrack(s, t - item, cand[i + 1:])
        #         s.pop()
        #
        # backtrack([], target, candidates)
        # return ans

        # 参考题解：https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/

        def dfs(begin, remain, s):
            if remain == 0:
                ans.append(s[:])
                return

            for index in range(begin, n):
                if candidates[index] > remain:
                    break
                if candidates[index -1] == candidates[index] and index > begin:
                    continue
                s.append(candidates[index])
                dfs(index + 1, remain - candidates[index], s)
                s.pop()

        dfs(0, target, [])
        return ans


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
# candidates = [2, 5, 2, 1, 2]
# target = 5
res = Solution().combinationSum(candidates, target)
print(res)
