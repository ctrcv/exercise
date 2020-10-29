class Solution:
    def threeOrders(self, root):
        preorder = []
        inorder = []
        postorder = []

        def find(node):
            if node is None:
                return []

            preorder.append(node.val)
            find(node.left)
            inorder.append(node.val)
            find(node.right)
            postorder.append(node.val)

        find(root)
        res = [preorder, inorder, postorder]
        return res

    # def preorder(self, node):
    #     if node is None:
    #         return
    #     self.pre.append(node.val)
    #     self.preorder(node.left)
    #     self.preorder(node.right)
    #
    # def inorder(self, node):
    #     if node is None:
    #         return
    #
    #     self.inorder(node.left)
    #     self.vin.append(node.val)
    #     self.vin.append(node.right)
    #
    # def postorder(self, node):
    #     if node is None:
    #         return
    #     self.postorder(node.left)
    #     self.postorder(node.right)
    #     self.post.append(node.val)
