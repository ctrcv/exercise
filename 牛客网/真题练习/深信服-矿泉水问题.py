# class Solution:
#     def mincost(self, x, a, b):
#         if x <= 0:
#             return 0
#         a3 = a * 3
#         t = min(a3, b)
#         cost = x // 1500 * t
#         r = x % 1500
#
#         p1 = int(r / 500 + 0.5) * a
#         rest_mincost = min(p1, b)
#
#         ans = cost + rest_mincost
#         return ans
#
#
def Mincost(x, a, b):
    if x <= 0:
        return 0
    a3 = a * 3
    t = min(a3, b)
    cost = x // 1500 * t
    r = x % 1500

    p1 = int(r / 500 + 0.5) * a
    rest_mincost = min(p1, b)

    ans = cost + rest_mincost
    return ans


N = int(input())
# solution = Solution()
for i in range(N):
    X, A, B = input().strip().split()
    # print(solution.mincost(int(X), int(A), int(B)))
    print(Mincost(int(X), int(A), int(B)))

# import math
#
#
# class Solution():
#     def f(self, x, a, b):
#         a3 = 3 * a
#         min_p = min(a3, b)
#         base_p = x // 1500 * min_p
#         rest = x % 1500
#         use_a = math.ceil(rest / 500) * a
#         rest_p = min(use_a, b)
#         return base_p + rest_p
#
#
# n = int(input().strip())
# sol = Solution()
# for i in range(n):
#     line = [int(item) for item in input().strip().split()]
#     res = sol.f(*line)
#     print(res)
