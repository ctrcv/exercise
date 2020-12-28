# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归实现，DFS
# 后序遍历
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return root
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         # 先序遍历或后序遍历都可以实现， 此处使用后序遍历实现
#         root.left, root.right = root.right, root.left
#
#         return root

# 迭代实现，BFS
# 先序遍历实现
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
