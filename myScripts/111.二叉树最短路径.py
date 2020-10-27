class Solution:
    def minDepth(self, root):

        # 广度优先搜索BFS
        # from queue import Queue
        # if root is None:
        #     return 0
        # depth = 1
        # queue = Queue()
        # queue.put(root)
        #
        # while not queue.empty():
        #     sz = queue.qsize()
        #     for i in range(sz):
        #         curr = queue.get()
        #         if curr.left is None and curr.right is None:
        #             return depth
        #
        #         if curr.left is not None:
        #             queue.put(curr.left)
        #         if curr.right is not None:
        #             queue.put(curr.right)
        #
        #     depth += 1
        #
        # return depth

        # 深度优先搜索DFS1
        # if root is None:
        #     return 0
        # if root.left is None and root.right is None:
        #     return 1
        # min_depth = float('INF')
        # if root.left:
        #     min_depth = min(self.minDepth(root.left), min_depth)
        # if root.right:
        #     min_depth = min(self.minDepth(root.right), min_depth)
        #
        # return min_depth + 1

        # 深度优先搜索DFS2
        if root is None:
            return 0
        depth = 1
        if root.left and root.right:
            depth += min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            depth += self.minDepth(root.left)
        elif root.right:
            depth += self.minDepth(root.right)

        return depth




