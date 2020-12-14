# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法1。迭代法。时间复杂度为O(L1+L2),空间复杂度O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        pHead = ListNode()
        p = pHead
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        # 将l1或l2链表中剩余的元素加入链表
        p.next = l1 if l1 else l2

        return pHead.next

# # 方法2.递归。时间复杂度O(L1+L2),空间复杂度O(L1+L2)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


L1, L2 = 3, 3
p1, p2 = ListNode(), ListNode()
pt1, pt2 = p1, p2
print("第一个链表")
for i in range(L1):
    x = int(input())
    pt1.next = ListNode(x)
    pt1 = pt1.next

print("第二个链表")
for i in range(L2):
    x = int(input())
    pt2.next = ListNode(x)
    pt2 = pt2.next

print("输出结果")
res = Solution().mergeTwoLists(p1.next, p2.next)
while res:
    print(res.val)
    res = res.next
