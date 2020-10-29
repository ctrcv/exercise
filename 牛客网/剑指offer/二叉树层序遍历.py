# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型二维数组
#
class Solution:
    def levelOrder(self, root):
        # write code here
        if root is None:
            return [[]]
        import queue
        res = []
        def bfs(root):
            que = queue.Queue()
            que.put(root)

            while not que.empty():
                sz = que.qsize()
                tmp = []
                for i in range(sz):
                    node = que.get()
                    tmp.append(node.val)

                    if node.left is not None:
                        que.put(node.left)
                    if node.right is not None:
                        que.put(node.right)
                res.append(tmp)
        bfs(root)
        return res





