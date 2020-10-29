# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        flag = False
        if (pRoot1 is not None) and (pRoot2 is not None):
            # 如果使用if not pRoot1 and not pRoot2: 整个会被直接判定成Flase，if内的语句不会被执行
            flag = self.DoesTree1HasTree2(pRoot1, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.left, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.right, pRoot2)

        return flag

    def DoesTree1HasTree2(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False

        if root1.val == root2.val:
            return self.DoesTree1HasTree2(root1.left, root2.left) and \
                   self.DoesTree1HasTree2(root1.right, root2.right)
        else:
            return False


t1 = TreeNode(8)
t1.left = TreeNode(8)
t1.right = TreeNode(7)
t1.left.left = TreeNode(9)
t1.left.right = TreeNode(2)
t1.left.right.left = TreeNode(4)
t1.left.right.right = TreeNode(7)


t2 = TreeNode(8)
t2.left = TreeNode(9)
t2.right = TreeNode(2)

print(Solution().HasSubtree(t1, t2))


