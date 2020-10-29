# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        head = ListNode(None)
        cur = head

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next

            cur = cur.next

        cur.next = pHead1 if pHead1 else pHead2
        return head.next


p1 = ListNode(2)
p1.next = ListNode(3)
p1.next.next = ListNode(5)

p2 = ListNode(3)
p2.next = ListNode(7)

p = Solution().Merge(p1, p2)
while p:
    print(p.val)
    p = p.next
