# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    pre = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 方法：后序遍历。 因为使用前序遍历会导致的话，会导致右孩子丢失
        # 而后续遍历不会，因为更新当前的右指针的时候，当前节点的右孩子已经访问过了
        # 依次遍历 6 5 4 3 2 1，然后每遍历一个节点就将当前节点的右指针更新为上一个节点pre

        # 递归版，可运行
        # if not root:
        #     return
        # self.flatten(root.right)
        # self.flatten(root.left)
        # root.right = self.pre
        # root.left = None
        # self.pre = root

        # 迭代版,，改版代码有问题
        # stack = []
        # pre, curr = None, root
        #
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.right
        #
        #     curr = stack.pop()
        #     # 在不存在左节点或右节点已经访问过的情况下，访问根节点
        #     if not curr.left or curr == pre:
        #
        #         curr.right = pre
        #         curr.left = None
        #         pre = curr
        #         # curr = None
        #     else:
        #         # 左节点还没有访问过就先访问左节点
        #         curr = curr.left

        # 官方题解
        # 1. 前序遍历.

        # 前序遍历思路：读取每个节点，并使用链表进行存储，
        # 之后顺序读取列表，对每个节点进行左孩子等于空，右孩子等于下一个节点
        # 因为前序遍历对节点进行操作会破坏树的原结构
        # 所以需要额外的存储空间O(n)，但是是属于在链表原地进行操作的
        # preorderList = list()
        #
        # def preorderTraversal(root: TreeNode):
        #     if root:
        #         preorderList.append(root)
        #         preorderTraversal(root.left)
        #         preorderTraversal(root.right)
        #
        # preorderTraversal(root)
        # size = len(preorderList)
        # for i in range(1, size):
        #     prev, curr = preorderList[i - 1], preorderList[i]
        #     prev.left = None
        #     prev.right = curr

        # 1. 前序遍历迭代版，
        # preorderList = list()
        # stack = list()
        # node = root
        #
        # while node or stack:
        #     while node:
        #         preorderList.append(node)
        #         stack.append(node)
        #         node = node.left
        #     node = stack.pop()
        #     node = node.right
        #
        # size = len(preorderList)
        # for i in range(1, size):
        #     prev, curr = preorderList[i - 1], preorderList[i]
        #     prev.left = None
        #     prev.right = curr

        # 2。前序遍历和展开同步进行，该方法只能通过迭代的形式实现，因为栈需要同时保存两个节点
        # 思想：每次从栈内弹出一个节点作为当前访问的节点，获得该节点的子节点，
        # 如果子节点不为空，则依次将右子节点和左子节点压入栈内（注意入栈顺序）
        # 时间复杂度：O(n)，空间复杂度为O(n)，因为空间复杂度取决于栈的大小，栈的大小取决于节点的数目
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr

        # 3. 寻找前驱节点，空间复杂度O(1)
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
