# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # paths = []
        #
        # def dfs(node, path):
        #     path.append(str(node.val))
        #     if not node.left and not node.right:
        #         # print (path)
        #         paths.append(''.join(path))
        #         return
        #
        #     if node.left:
        #         dfs(node.left, path)
        #         path.pop()
        #     if node.right:
        #         dfs(node.right, path)
        #         path.pop()
        #
        # dfs(root, [])
        # tmp = [int(s) for s in paths]
        # ret = sum(tmp)
        # return ret

        def dfs(node, prevTotal):
            if not node:
                return 0
            total = prevTotal * 10 + node.val
            if not node.left and not node.right:
                return total
            else:
                dfs(node.left, total) + dfs(node.right, total)

        return dfs(root, 0)