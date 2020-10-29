class Solution:
    def __init__(self):
        self.result = []

    def printListNode(self, listNode):
        if listNode is None:
            return []
        self.dfs(listNode)
        return self.result

    def dfs(self, node):
        if node is None:
            return

        self.dfs(node.next)
        self.result.append(node.val)
