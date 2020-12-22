from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归法。时间 & 空间 O(n)。空间复杂度取决于递归的栈深度，而栈深度在二叉树为一条链的情况下会达到 O(n)的级别。
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#
#         def helper(node):
#             if not node: return
#             helper(node.left)
#             res.append(node.val)
#             helper(node.right)
#
#         helper(root)
#         return res

# 迭代法：用栈模拟还原递归方法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack:
            # 遍历到左子树底部
            while root:
                stack.append(root)
                root = root.left
            # 取值
            root = stack.pop()
            res.append(root.val)
            # 遍历右子树
            root = root.right

        return res
