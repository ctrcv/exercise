# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. 递归实现，时间空间O(n)
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         # 递归到最后一个节点， 该结点就是反转后的头结点
#         tail = self.reverseList(head.next)
#         # 让当前结点的下一个结点的next 指针指向当前节点
#         head.next.next = head
#         # 容易忽略使头节点指向空，否则会出现循环
#         head.next = None
#         return tail

# 迭代实现，时间O(n)，空间O(1)
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#
#         pre = None
#         curr = head
#         while curr:
#             tmp = curr.next
#             curr.next = pre
#             pre = curr
#             curr = tmp
#         return pre

# 双指针
# 定义指针 curr，初始化为 head .
# 每次都让 head 下一个结点的 next 指向 curr ，实现一次局部反转
# 局部反转完成之后，curr 和 head 的 next 指针同时 往前移动一个位置
# 循环上述过程，直至 curr 到达链表的最后一个结点
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        curr = head
        while head.next:
            tmp = head.next.next
            head.next.next = curr
            curr = head.next
            head.next = tmp

        return curr



