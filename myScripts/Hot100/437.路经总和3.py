# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# # 方法1：双递归
# class Solution:
#     res = 0
#
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         if not root:
#             return 0
#
#         def dfs(node, val):
#             if not node:
#                 return
#             val += node.val
#             if val == sum:
#                 self.res += 1
#
#             dfs(node.left, val)
#             dfs(node.right, val)
#
#         dfs(root, 0)
#         self.pathSum(root.left, sum)
#         self.pathSum(root.right, sum)
#
#         return self.res

# 方法2：前缀和
# 时间空间复杂度均为O(N)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # key是前缀和，value是大小为key的前缀和出现次数
        prefixSumCount = {}
        # 前缀和为0的路径
        prefixSumCount[0] = 1
        return self.recursionPathSum(root, prefixSumCount, sum, 0)

    def recursionPathSum(self, node, prefixSumCount, target, currSum):
        # 1. 递归的终止条件
        if not node:
            return 0
        # 2.本层的操作
        res = 0
        # 当前路径和
        currSum += node.val

        # 看看root到当前节点这条路上是否存在节点前缀和加target为currSum的路径
        #  当前节点->root节点反推，有且仅有一条路径，如果此前有和为currSum-target,而当前的和又为currSum,两者的差就肯定为target了
        # currSum-target相当于找路径的起点，起点的sum+target=currSum，当前点到起点的距离就是target
        res += prefixSumCount.get(currSum - target, 0)
        # 更新路径上当前节点前缀和的个数
        prefixSumCount[currSum] = prefixSumCount.get(currSum, 0) + 1

        # 3.进入下一层
        res += self.recursionPathSum(node.left, prefixSumCount, target, currSum)
        res += self.recursionPathSum(node.right, prefixSumCount, target, currSum)

        # 回到本层，回溯恢复状态
        prefixSumCount[currSum] = prefixSumCount.get(currSum) - 1
        return res
