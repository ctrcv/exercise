from typing import List


# 1. 并查集
# 时间复杂度：O((N + Q)logA),N为equations的长度，A是equations里不同字符的个数， Q是queries的长度
#   构建并查集O(NlogA),每次进行合并操作log(A)
#   查询并查集O(QlogA),每一次进行路径压缩O(logA)
# 空间复杂度：O(A)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equationSize = len(equations)
        unionFind = UnionFind(2 * equationSize)  # 一个item包含两个变量
        # 第一步：预处理，使用哈希表将变量值与id映射，方便编码查询
        hashMap = {}
        iD = 0
        for i in range(equationSize):
            var1, var2 = equations[i]

            if var1 not in hashMap:
                hashMap[var1] = iD
                iD += 1
            if var2 not in hashMap:
                hashMap[var2] = iD
                iD += 1
            unionFind.union(hashMap[var1], hashMap[var2], values[i])

        # 第二步：做查询
        querySize = len(queries)
        res = [0.0] * querySize
        for i in range(querySize):
            var1, var2 = queries[i]
            id1, id2 = hashMap.get(var1, -1), hashMap.get(var2, -1)

            # if (not id1) or (not id2):  # 直接not的形式有错，因为当id=0时，not 0 的结果是True
            if id1 < 0 or id2 < 0:
                res[i] = -1.0
            else:
                res[i] = unionFind.isConnected(id1, id2)

        return res


class UnionFind:
    def __init__(self, n):
        # 初始时，将每个节点的父节点都指向自身,
        self.parent = [i for i in range(n)]  # 父节点列表.
        self.weight = [1.0] * n  # 有向边的权重。
        # parent[a] = a表示b的父节点为a
        # 与之对应的有向边权重，记为weight[a] = 3, 表示节点a到到它的直接父节点的有向边权重

    # 并
    def union(self, x, y, value):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        self.parent[rootx] = rooty
        self.weight[rootx] = self.weight[y] * value / self.weight[x]

    # 查
    def find(self, x):
        """
        查询，并同时进行路径压缩
        :param x:
        :return: 根节点的id
        """
        # 如果当前节点的父节点不是根节点（根节点的值与自身相同）
        # 说明树的深度大于2，进行路径压缩
        # 一边查询一边修改结点指向是并查集的特色
        if x != self.parent[x]:
            # 在查询节点x的根节点的同时
            # 把节点x到根节点的沿途的所有节点的父节点都指向根节点
            # x节点的权值更新为路径权值的乘积
            origin = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] *= self.weight[origin]

        return self.parent[x]

    def isConnected(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return self.weight[x] / self.weight[y]
        else:
            return -1.0

# import queue
# # 2. 广度优先搜索（未完成）
# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         iD = 0
#         equationSize = len(equations)
#         hashMap = {}
#         for i in range(equationSize):
#             var1, var2 = equations[i]
#             if var1 not in hashMap:
#                 hashMap[var1] = iD
#                 iD += 1
#             if var2 not in hashMap:
#                 hashMap[var2] = iD
#                 iD += 1
#
#         # 对于每个点，存储其直接连接到的所有点及对应的权值
#         edge = []
#         for i in range(equationSize):
#             var1, var2 = equations[i]
#             va, vb = hashMap[var1], hashMap[var2]
#             edge[va] = (vb, values[i])
#             edge[vb] = (va, 1.0 / values[i])
#
#         queriesSize = len(queries)
#         res = [-1.0] * queriesSize
#         for i in range(queriesSize):
#             var1, var2 = queries[i]
#             result = -1.0
#             if (var1 in hashMap) and (var2 in hashMap):
#                 if var1 == var2:
#                     result = 1.0
#                 else:
#                     que = queue.Queue()




Eq = [["a", "b"], ["b", "c"]]
Values = [2.0, 3.0]
Queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(Solution().calcEquation(Eq, Values, Queries))
