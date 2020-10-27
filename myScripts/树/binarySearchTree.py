class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        print(root.key, end=' ')
        self._inorder(root.right)

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return TreeNode(key=data)

        if data < root.key:
            root.left = self._insert(root.left, data)
        elif data > root.key:
            root.right = self._insert(root.right, data)
        else:
            raise ValueError('The tree has already exist key \'%d\'' % data)

        return root

    def delete(self, data):
        self._delete(self.root, data)

    def _delete(self, root, data):
        if not root:
            raise ValueError('not found data')

        if data < root.key:
            root.left = self._delete(root.left, data)
        elif data > root.key:
            root.right = self._delete(root.right, data)

        elif root.left and root.right:
            right_min = self._findMin(self.root.right)
            root.key = right_min.key
            root.right = self._delete(root.right, right_min.key)
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = None

        return root

    def _findMin(self, root):
        if not root.left:
            return root
        return self._findMin(root.left)

    def print_tree(self):
        if not self.root:
            return
        import queue
        que = queue.Queue()
        que.put(self.root)

        while not que.empty():
            sz = que.qsize()
            s = ''
            for i in range(sz):
                node = que.get()
                s += str(node.key)
                if i != sz - 1:
                    s += str(' ')

                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)
            print(s)


# 参考：https://blog.csdn.net/hjj414/article/details/37700843?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
if __name__ == '__main__':

    datas = [5, 2, 3, 8, 6, 9, 1, 11]
    bt = BinarySearchTree()
    for d in datas:
        bt.insert(d)

    # bt.inorder()
    bt.print_tree()
    bt.delete(11)
    bt.print_tree()
    bt.inorder()
    # bt.delete(11)
    bt.insert(8)
