# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return
        p1 = head
        p2 = head

        cnt = 0
        while p1.next:
            p1 = p1.next

            cnt += 1
            if cnt >= k:
                p2 = p2.next
        if cnt < k - 1:
            return
        else:
            return p2
