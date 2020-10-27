class Solution(object):
    def letterCombinations(self, digits: str) -> list:
        query_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits: return []

        # 方法1：非回溯
        # res = []
        # for x in digits:
        #     if x.isdigit() and x != '1':
        #
        #         if not res:
        #             res = [t for t in query_map[x]]
        #         else:
        #             tmp = []
        #             for i in range(len(query_map[x])):
        #                 for e in res:
        #                     tmp.append(e + query_map[x][i])
        #             res = tmp
        #
        # return res

        # 方法2：动态规划思想
        # res = ['']
        # for digit in digits:
        #     res = [r + d for r in res for d in query_map[digit]]
        #
        # return res

        # 方法3：回溯
        # def backtrack(combination, nextdigit):
        #     if len(nextdigit) == 0:
        #         res.append(combination)
        #         return res
        #
        #     # else:
        #     for letters in query_map[nextdigit[0]]:
        #         for letter in letters:
        #             backtrack(combination + letter, nextdigit[1:])
        #
        # res = []
        # backtrack('', digits)
        # return res

        # 方法4：队列
        queue = ['']
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for d in query_map[digit]:

                    queue.append(tmp + d)

        return queue




r = Solution().letterCombinations('234')
print(r)
