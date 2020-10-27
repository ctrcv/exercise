class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        # 自写
        ans = []

        def backtrack(S, t, cand):
            if t == 0:
                # print(S)
                ans.append([]+S)
                # ans.append(S)  #直接append（S）会出现ans为None，
                # 原因参考：https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/517130
                return
            if t < 0:
                return

            for i, item in enumerate(cand):
                S.append(item)
                backtrack(S, t - item, cand[i:])
                S.pop()

        backtrack([], target, candidates)
        return ans

        # 题解
        # candidates = sorted(candidates)
        #
        # ans = []
        #
        # def find(s, use, remain):
        #     for i in range(s, len(candidates)):
        #         c = candidates[i]
        #         if c == remain:
        #             ans.append(use + [c])
        #         if c < remain:
        #             find(i, use + [c], remain - c)
        #         if c > remain:
        #             return
        #
        # find(0, [], target)
        #
        # return ans


candidates = [2, 3, 5]
target = 8
s = Solution().combinationSum(candidates, target)
print(s)
