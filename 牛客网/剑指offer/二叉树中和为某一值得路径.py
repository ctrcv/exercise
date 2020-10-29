# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        paths = []

        def backtrack(path, s, node):
            if not node:
                return
            if s == node.val and not node.left and not node.right:
                paths.append(path[:])

            path.append(node.val)
            backtrack(path, s - node.val, node.left)
            backtrack(path, s - node.val, node.right)
            path.pop()

        backtrack([], expectNumber, root)

        return paths
