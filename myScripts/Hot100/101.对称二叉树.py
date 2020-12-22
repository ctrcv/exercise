# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 递归，时间空间复杂度均为O(n)
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def helper(node1, node2):
    #         # 如果同时到达树底，返回True
    #         if not node1 and not node2:
    #             return True
    #         # 如果左右子树形状不同，返回False
    #         if not node1 or not node2:
    #             return False
    #         # 判断节点值是否相同，左子树左节点和右节点、右节点和左节点是否相同
    #         if node1.val != node2.val:
    #             return False
    #         return helper(node1.left, node2.right) and helper(node1.right, node2.left)
    #
    #     if not root:
    #         return True
    #     return helper(root.left, root.right)

    # 迭代
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        # 使用队列保存节点
        queue = [root.left, root.right]
        while queue:
            # 从队列中取出两个节点
            left = queue.pop(0)
            right = queue.pop(0)
            # 如果两个节点同时为空则继续循环，只有一个为空则跳出循环
            if not left and not right:
                continue
            if not left or not right:
                return False
            # 比较两个节点值是否相同
            if left.val != right.val:
                return False
            # 将左节点的左节点，右节点的右节点放入队列
            queue.append(left.left)
            queue.append(right.right)
            # 将左节点的右节点，右节点的左节点放入队列
            queue.append(left.right)
            queue.append(right.left)

        return True
