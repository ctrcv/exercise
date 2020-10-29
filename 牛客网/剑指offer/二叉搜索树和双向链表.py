# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        lastNodeInList = self.convertNode(pRootOfTree, None)
        while lastNodeInList.left:
            lastNodeInList = lastNodeInList.left

        return lastNodeInList

    def convertNode(self, node, lastNode):
        if not node:
            return

        pCurrent = node
        if pCurrent.left:
            lastNode = self.convertNode(pCurrent.left, lastNode)

        pCurrent.left = lastNode
        if lastNode:
            lastNode.right = pCurrent

        lastNode = pCurrent
        if pCurrent.right:
            lastNode = self.convertNode(pCurrent.right, lastNode)

        return lastNode
