# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = p = ListNode()
        # print(res is None)
        flag = 0
        while l1.next is not None and l2.next is not None:
            s = l1.val + l2.val
            if s >= 10:
                p.val = s % 10 + flag
                flag = 1
            else:
                p.val = s + flag
                flag = 0

            p.next = ListNode()
            p = p.next
            l1 = l1.next
            l2 = l2.next

        while l1.next:
            p.next = l1
            l1 = l1.next
        while l2.next:
            p.next = l2
            l2 = l2.next
        if p.val >= 10:
            t = p.val
            p.val = 1
            p.next = ListNode(t - 10)
        return res


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

# while head1.next:
#     print(head1.val)
#     head1 = head1.next
#
# while head2.next:
#     print(head2.val)
#     head2 = head2.next
