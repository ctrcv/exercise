from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = {}
        ans = 0
        for m in range(len(A)):
            for n in range(len(B)):
                s1 = A[m] + B[n]
                dic[s1] = dic.get(s1, 0) + 1

        for i in range(len(C)):
            for j in range(len(D)):
                s2 = -C[i] - D[j]
                if s2 in dic:
                    ans += dic[s2]

        return ans


A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(Solution().fourSumCount(A, B, C, D))
