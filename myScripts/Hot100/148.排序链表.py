# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 自顶向下归并排序。时间复杂度O(nlogn), 空间复杂度O(logn),因为递归需要栈空间
# 找到链表的中点，以中点为分界，将链表拆分成两个子链表。
# 寻找链表的中点可以使用快慢指针的做法，快指针每次移动2步，慢指针每次移动1步，当快指针到达链表末尾时，慢指针指向的链表节点即为链表的中点。
# 对两个子链表分别排序。
# 将两个排序后的子链表合并，得到完整的排序后的链表。可以使用「21. 合并两个有序链表」的做法，将两个有序的子链表进行合并

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)

# 自底向上排序。时间复杂度，O（nlogn）,空间复杂度O(1)
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         def merge(head1: ListNode, head2: ListNode) -> ListNode:
#             dummyHead = ListNode(0)
#             temp, temp1, temp2 = dummyHead, head1, head2
#             while temp1 and temp2:
#                 if temp1.val <= temp2.val:
#                     temp.next = temp1
#                     temp1 = temp1.next
#                 else:
#                     temp.next = temp2
#                     temp2 = temp2.next
#                 temp = temp.next
#             if temp1:
#                 temp.next = temp1
#             elif temp2:
#                 temp.next = temp2
#             return dummyHead.next
#
#         if not head:
#             return head
#
#         length = 0
#         node = head
#         while node:
#             length += 1
#             node = node.next
#
#         dummyHead = ListNode(0, head)
#         subLength = 1
#         while subLength < length:
#             prev, curr = dummyHead, dummyHead.next
#             while curr:
#                 head1 = curr
#                 for i in range(1, subLength):
#                     if curr.next:
#                         curr = curr.next
#                     else:
#                         break
#                 head2 = curr.next
#                 curr.next = None
#                 curr = head2
#                 for i in range(1, subLength):
#                     if curr and curr.next:
#                         curr = curr.next
#                     else:
#                         break
#
#                 succ = None
#                 if curr:
#                     succ = curr.next
#                     curr.next = None
#
#                 merged = merge(head1, head2)
#                 prev.next = merged
#                 while prev.next:
#                     prev = prev.next
#                 curr = succ
#             subLength <<= 1
#
#         return dummyHead.next



# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# # 二叉搜索树的建立
# def sortedTree(nums):
#     def builder(node, head):
#         if node.val <= head.val:
#             if not head.left:
#                 head.left = node
#             else:
#                 builder(node, head.left)
#         else:
#             if not head.right:
#                 head.right = node
#             else:
#                 builder(node, head.right)
#
#     if not nums:
#         return
#     root = TreeNode(nums[0])
#     for i in range(1, len(nums)):
#         node = TreeNode(nums[i])
#         builder(node, root)
#
#     return root
#
#
# def inorder(node):
#     if not node:
#         return
#
#     inorder(node.left)
#     sorted_tree.append(node.val)
#     inorder(node.right)


if __name__ == "__main__":
    Nums = [4, 2, 2, 3]
    root = sortedTree(Nums)
    sorted_tree = []
    inorder(root)
    print(sorted_tree)
