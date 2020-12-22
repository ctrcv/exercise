# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 本题关键在于要先设定一个虚拟的值为极小值的根节点，
# 有了初始的虚拟根节点后，无论是使用递归还是迭代，或者三种遍历方式中的哪一个，都相对容易解决
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归1:
        # def helper(node, lower=float("-inf"), upper=float("inf")):
        #     if not node: return True
        #     val = node.val
        #     if val <= lower or val >= upper: return False
        #     if not helper(node.left, lower, val): return False
        #     if not helper(node.right, val, upper): return False
        #     return True
        # return helper(root)
        #
        # # 中序遍历，迭代版
        stack, inorder = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

    # 中序遍历，递归版
    # pre = float("-inf")
    #
    # def isValidBST(self, root: TreeNode) -> bool:
    #     if not root: return True
    #     # 访问左子树
    #     if not self.isValidBST(root.left):
    #         return False
    #     # 访问当前节点：如果当前节点小于等于中序遍历的前一个节点，说明不满足BST，返回 false；否则继续遍历
    #     if root.val <= self.pre:
    #         return False
    #     self.pre = root.val
    #     # 访问右子树
    #     if not self.isValidBST(root.right):
    #         return False
    #     return True

