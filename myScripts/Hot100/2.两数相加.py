# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = p = ListNode()
        flag = 0
        while l1 or l2 or flag:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + flag
            p.next = ListNode(s % 10)
            p = p.next
            flag = s // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


head1 = L1 = ListNode()
head2 = L2 = ListNode()
print("L1 input")
for i in range(5):
    L1.val = int(input())
    L1.next = ListNode()
    L1 = L1.next

print("L2 input")
for j in range(3):
    L2.val = int(input())
    L2.next = ListNode()
    L2 = L2.next

ans = Solution().addTwoNumbers(head1, head2)
while ans.next:
    print(ans.val)
    ans = ans.next
