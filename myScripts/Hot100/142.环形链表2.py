# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        # 先判断是否有环，如果有环，快指针的速度是慢指针的2倍，迟早会相遇
        while True:
            # 如果只有一个节点，则直接返回
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break

        # 有环的话，快慢指针相遇的节点不一定是环的入口节点
        # 相遇的节点与环入口节点的距离与链表头节点到环入口的距离相等，假设为a
        # 所以需要慢指针继续走指针a步才能到环入口
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
