# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 对任意一颗二叉树而言，前序遍历的形式总是：[ 根节点, [左子树的前序遍历结果], [右子树的前序遍历结果] ]
        # 中序遍历的形式总是：[ [左子树的中序遍历结果], 根节点, [右子树的中序遍历结果] ]

        # 递归实现
        def builder(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return

            # 前序遍历的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历的结果中获得根节点的索引
            inorder_root = index[preorder[preorder_root]]

            # 建立根节点
            root = TreeNode(preorder[preorder_root])
            # 获取左节点的节点数目
            left_treesize = inorder_root - inorder_left
            # 递归构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 left_treesize」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = builder(preorder_left + 1, preorder_left + left_treesize,
                                inorder_left, inorder_root - 1)
            # 递归构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = builder(preorder_left + left_treesize + 1, preorder_right,
                                 inorder_root + 1, inorder_right)

            return root

        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        return builder(0, n - 1, 0, n - 1)

        # 迭代实现
        # if not preorder:
        #     return None
        #
        # root = TreeNode(preorder[0])
        # stack = [root]
        # inorderIndex = 0
        # for i in range(1, len(preorder)):
        #     preorderVal = preorder[i]
        #     node = stack[-1]
        #     if node.val != inorder[inorderIndex]:
        #         node.left = TreeNode(preorderVal)
        #         stack.append(node.left)
        #     else:
        #         while stack and stack[-1].val == inorder[inorderIndex]:
        #             node = stack.pop()
        #             inorderIndex += 1
        #         node.right = TreeNode(preorderVal)
        #         stack.append(node.right)
        #
        # return root

