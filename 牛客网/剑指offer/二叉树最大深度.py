def maxDepth(root):
    def dfs(node):
        if node is None:
            return 0
        return max(dfs(node.left), dfs(node.right)) + 1

    # def bfs(node):
    #     if node is None:
    #         return 0
    #     import queue
    #     que = queue.Queue()
    #     que.put(node)
    #     depth = 1
    #     while que:
    #         sz = que.qsize()
    #         for i in range(sz):
    #             x = que.get()
    #
    #             if x.left:
    #                 que.put(x.left)
    #             if x.right:
    #                 que.put(x.right)
    #         depth += 1
    #     return depth

    return dfs(root)
    # return bfs(root)
