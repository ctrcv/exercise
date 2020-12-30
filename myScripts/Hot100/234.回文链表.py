# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法1：遍历链表，每个元素逐个存储后对比翻转的数组与未翻转的数组是否相同
# 方法2：递归
# 方法3： 快慢指针
# 主要思想：先找到链表的中点，然后使用中心扩散的思想
# 情况要分奇数个节点的情况和偶数个节点的情况
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # 分别获得两个子链表的尾节点和首节点
        first_half_end = self._find_middle(head)
        second_half_start = self._reverse(first_half_end.next)
        # 判断回文
        flag = True
        p1, p2 = head, second_half_start
        while flag and p2:
            if p1.val != p2.val:
                flag = False
            p1 = p1.next
            p2 = p2.next
        # 将后半部分的链表还原
        first_half_end.next = self._reverse(second_half_start)
        return flag

    # 找中心点
    def _find_middle(self, head):
        slow = fast = head
        # fast.next 为空， 偶数个节点
        # fast为空，奇数个节点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 链表翻转
    def _reverse(self, head):
        pre, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp

        return pre
