# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here

        # 1. 先复制普通节点，再复制随机节点
        if not pHead:
            return
        p = pHead
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p


        # 2. 使用字典降低查找的复杂度
        # if not pHead:
        #     return
        # hashmap = dict()
        # p = pHead
        #
        # while p:
        #     node = RandomListNode(p.label)
        #     hashmap[p] = node
        #     p = p.next
        #
        # p = pHead
        # while p:
        #     node = hashmap[p]
        #     if p.next:
        #         node.next = hashmap[p.next]
        #     if p.random:
        #         node.random = hashmap[p.random]
        #
        #     p = p.next
        # return hashmap[pHead]

