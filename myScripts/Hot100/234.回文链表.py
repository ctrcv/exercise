# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 主要思想：先找到链表的中点，然后使用中心扩散的思想
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
