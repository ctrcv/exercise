""" 最长不重复子串"""
# def lengthOfLongestSubstring(ss):
#     if not ss:
#         return 0
#
#     left, right = 0, 0
#     hashset = set()
#     maxlen = 0
#     n = len(ss)
#     while right < n:
#         if ss[right] not in hashset:
#             hashset.add(ss[right])
#             right += 1
#             if len(hashset) > maxlen:
#                 maxlen = len(hashset)
#         elif left < right:
#             left += 1
#             hashset.discard(ss[right])
#
#     return maxlen
#
#
# S = 'abcabcbb'
# print(lengthOfLongestSubstring(S))

""" x的n次方 """
# def myPower(x, n):
#     if n == 0:
#         return 1
#     if x == 0:
#         return 0
#
#     if n < 0:
#         x = 1 / x
#         n *= -1
#
#     # tmp = myPower(x, n // 2)
#     # if n % 2 == 0:
#     #     return tmp * tmp
#     # else:
#     #     return x * tmp * tmp
#
#     res = 1
#     while n:
#         if n & 1:
#             res = x * res
#         x *= x
#         n >>= 1
#     return res
#
#
# X = 0.5
# N = -2
# print(myPower(X, N))


"""链表中的倒数第k个节点"""
# def lastkthnode(phead, k):
#     node1 = node2 = phead
#     # while k:
#     #     if node1:
#     #         node1 = node1.next
#     #     else:
#     #         return
#     #
#     # while node1:
#     #     node1 = node1.next
#     #     node2 = node2.next
#     #
#     # return node2
#     t = 0
#     while node1:
#         if t >= k: node2 = node2.next
#         node1 = node1.next
#         t += 1
#     return node2

"""二叉树深度"""
# def binaryDepth(root):
#     if not root:
#         return 0
#     return max(binaryDepth(root.left), binaryDepth(root.right)) + 1

"""二叉树最长路径"""
# def maxlenpath(root): # 未验证
#     if not root:
#         return root
#     global maxpath
#     maxpath = []
#
#     def dfs(path, node):
#         if not node:
#             global maxpath
#             if len(path) > len(maxpath):
#                 maxpath = path[:]
#         path.append(node)
#         dfs(path, node.left)
#         dfs(path, node.right)
#
#     dfs([], root)
#     return maxpath

"""二叉树路径和为给定值"""
# def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#     if not root:
#         return []
#
#     paths = []
#
#     def dfs(node, val, path):
#         if not node:
#             return
#         path.append(node.val)
#         if val == node.val and not node.left and not node.right:
#             paths.append(path[:])
#
#         if node.left:
#             dfs(node.left, val - node.val, path)
#         if node.right:
#             dfs(node.right, val - node.val, path)
#         path.pop()
#
#     dfs(root, sum, [])
#     return paths


"""二叉树最大路径和"""
# class Solution:
#     def dfs(self,node: TreeNode) ->int :
#         if node.left == None:
#             lm = 0
#         else:
#             lm = self.dfs(node.left)
#         if node.right == None:
#             rm = 0
#         else:
#             rm = self.dfs(node.right)
#         if max(lm+rm,0,rm,lm)+node.val > self.m:
#             self.m = max(lm+rm,0,rm,lm)+node.val
#         return max(lm,0,rm)+node.val
#
#     def maxPathSum(self, root: TreeNode) -> int:
#         self.m = -0xFFFFFFFF
#         self.dfs(root)
#         return self.m

"""判断链表对称/回文"""
# def isPalindrome(self, head: ListNode) -> bool:
#     if not head:
#         return True
#
#     phead = head
#     ptail = head
#     stack = []
#     k = 0
#     while ptail:
#         k += 1
#         stack.append(ptail)
#         ptail = ptail.next
#
#     k = k // 2
#     while k > 0:
#         ptail = stack.pop()
#         if phead.val != ptail.val:
#             return False
#         phead = phead.next
#         k -= 1
#
#     return True


"""链表反转"""
# def reverseList(self, head: ListNode) -> ListNode:
#     prev, curr = head, None
#     while prev:
#         t = prev.next
#         prev.next = curr
#         curr = prev
#         prev = t
#
#     return curr


"""青蛙爬楼梯"""
# def climbStairs(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     a, b = 1, 2
#     for i in range(3, n + 1):
#         # c = a + b
#         # a = b
#         # b = c
#         a, b = b, a + b
#
#     return b
#
# N = 3
# print(climbStairs(N))

"""连续子数组最大和"""
# def maxSubArray(nums) -> int:
#     if not nums:
#         return 0
#     n = len(nums)
#     # dp = [float('-inf')] * n
#     # maxsum = float('-inf')
#     # for i in range(n):
#     #     if i == 0:
#     #         dp[0] = nums[0]
#     #     else:
#     #         dp[i] = max(nums[i], dp[i - 1] + nums[i])
#     #         maxsum = max(maxsum, dp[i])
#     #
#     # return maxsum
#     for i in range(1, n):
#         nums[i] += max(nums[i - 1], 0)
#
#     return max(nums)
#
#
# Nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maxSubArray(Nums))


"""最长公共子序列"""

# def longestCommonSubsequence(text1: str, text2: str) -> int:
#     if not text1 or not text2:
#         return 0
#     m, n = len(text1), len(text2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if text1[i - 1] == text2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][ j - 1])
#
#     return dp[m][n]
#
#
# # T1 = "abcde"
# T1 = "abc"
# T2 = 'ace'
# print(longestCommonSubsequence(T1, T2))

"""partition"""
from random import randint


def partition(arr, start, end):
    pivotIndex = randint(start, end)
    pivotValue = arr[pivotIndex]
    arr[end], arr[pivotIndex] = arr[pivotIndex], arr[end]
    storeIndex = start
    # print('pivot index', pivotIndex, pivotValue)
    while start < end:
        if arr[start] < pivotValue:
            arr[storeIndex], arr[start] = arr[start], arr[storeIndex]
            storeIndex += 1
        start += 1
        print(arr)

    arr[storeIndex], arr[end] = arr[end], arr[storeIndex]
    # print(arr)
    return storeIndex


# nums = [2, 6, 3, 4, 8, 62, 4, 32, 12, 5]
# print(partition(nums, 0, len(nums) - 1))


# TODO """最长连续公共子串"""

# 最小的k个数
def getLeastNumbers(arr, k):
    if not arr or k > len(arr):
        return arr
    if k <= 0:
        return []
    import heapq
    ret = []
    n = len(arr)
    for i in range(n):
        if len(ret) < k:
            heapq.heappush(ret, -arr[i])
        else:
            if ret[0] < -arr[i]:
                heapq.heapreplace(ret, -arr[i])

    return [-1 * item for item in ret]


nums = [4, 5, 1, 6, 2, 7, 3]
print(getLeastNumbers(nums, 4))
