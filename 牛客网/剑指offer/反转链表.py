# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode

    # 递归
    # def ReverseList(self, pHead):
    #     # write code here
    #     if pHead.next is None:
    #         return pHead
    #     if pHead is None:
    #         return pHead
    #
    #     headNode = self.ReverseList(pHead)
    #     pHead.next.next = pHead
    #     pHead.next = None
    #
    #     return headNode

    # 迭代
    # 1）pre指针指向已经反转好的链表的最后一个节点，最开始没有反转，所以指向nullptr
    # 2）cur指针指向待反转链表的第一个节点，最开始第一个节点待反转，所以指向head
    # 3）nex指针指向待反转链表的第二个节点，目的是保存链表，因为cur改变指向后，后面的链表则失效了，所以需要保存
    def ReverseList(self, pHead):
        if pHead.next is None:
            return pHead
        if pHead is None:
            return pHead

        pre = None
        curr = pHead

        while curr:
            nextNode = curr.next
            curr.next = pre
            pre, curr = curr, nextNode



