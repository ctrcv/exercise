# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        # 1. 递归 + 动态规划
        # 对于一个节点o,设f(o)表示选择节点o的情况下,o节点子树上被选择的节点的最大权值和;
        # g(o)表示不选择节点o的情况下,o节点子树上被选择的节点的最大权值和
        # left和right表示节点o的左右孩子

        # 当节点o被选中时, o的左右孩子都不能够再被选中,故在o节点被选中的情况下子树上被选中节点最大权值和为
        # 左节点left和右节点right不被选中的最大权值和相加
        # 即:f(0) = g(left) + g(right)

        # 当节点o没有被选中时,o的左右孩子节点可以被选中,也可以不被选中
        # 故g(o)= max(f(left), g(left)) + max(f(right), g(right))

        # 所以可以通过哈希映射表存储f和g的值,用DFS后序遍历二叉树,根节点对应的f和g中最大值即为所求

        # 该部分代码在测试用例[3,4,5,1,3,null,1]出现结果错误,预期结果为9,实际结果为8
        # 原因未知
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     dfs(root.right)
        #     f[root] = root.val + g.get(root.left, 0) + g.get(root.right, 0)
        #     g[root] = max(f.get(root.left, 0), g.get(root.left, 0) + max(f.get(root.right, 0), g.get(root.right, 0)))
        #
        # f, g = {}, {}
        # dfs(root)
        # return max(f.get(root, 0), g.get(root, 0))

        # 该部分代码可以通过所有的测试用例
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     dfs(root.right)
        #     f[root] = g[root.left] + g[root.right] + root.val
        #     g[root] = max(f[root.left], g[root.left]) + max(f[root.right], g[root.right])
        #
        # f = {None: 0}
        # g = {None: 0}
        # dfs(root)
        # return max(f[root], g[root])

        # 空间优化
        # f[o]和g[o]只与f[l], g[l], f[r], g[r]相关,所以只需要在返回时将f和g都返回,即可省掉哈希映射表的空间
        def _dfs(node):
            if not node:
                return [0, 0]
            left = _dfs(node.left)
            right = _dfs(node.right)
            selected = node.val + left[1] + right[1]
            notSelected = max(left[0], left[1]) + max(right[0], right[1])
            return [selected, notSelected]

        return max(_dfs(root))
