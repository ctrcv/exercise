# # -*- coding:utf-8 -*-
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# class Solution:
#     # 返回从上到下每个节点值列表，例：[1,2,3]
#     def PrintFromTopToBottom(self, root):
#         # write code here
#         if root is None:
#             return
#         import queue
#         que = queue.Queue()
#         que.put(root)
#         ans = []
#         while que:
#             # sz = que.qsize()
#
#             # for i in range(sz):
#             node = que.get()
#             ans.append(node.val)
#
#             if node.left:
#                 que.put(node.left)
#             if node.right:
#                 que.put(node.right)
#
#         return ans


### 以上使用自带库queue的代码在牛客网上运行超时

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        import queue
        que = queue.Queue()
        que.put(root)
        # que = [root]
        ans = []
        while not que:
            # sz = que.qsize()

            # for i in range(sz):
            node = que.get()
            # node = que.pop(0)
            ans.append(node.val)

            if node.left:
                que.put(node.left)
                # que.append(node.left)
            if node.right:
                que.put(node.right)
                # que.append(node.right)

        return ans
