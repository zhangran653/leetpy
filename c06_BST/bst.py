class BST:
    class _Node:
        def __init__(self, e):
            self.e = e
            self.left, self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, e):
        self._add(self._root, e)

    def _add(self, node, e):
        """
        if node.e == e:
            return
        if node.e < e and not node.right:
            node.right = self._Node(e)
            self._size += 1
            return
        elif node.e > e and not node.left:
            node.left = self._Node(e)
            self._size += 1
            return
        if node.e < e:
            self._add(node.right, e)
        else:
            self._add(node.left, e)
        :param node:
        :param e:
        :return: 插入节点后二分搜索树的根
        """
        if not node:
            self._size += 1
            return self._Node(e)
        if node.e < e:
            node.right = self._add(node.right, e)
        else:
            node.left = self._add(node.left, e)

        return node

    def contains(self, e):
        return self._contains(self._root, e)

    def _contains(self, node, e):
        if not node:
            return False

        if node.e == e:
            return True
        elif node.e > e:
            return self._contains(node.left, e)
        else:
            return self._contains(node.right, e)

    def pre_order(self):
        self._pre_order(self._root)

    def _pre_order(self, node):
        if not node:
            return
        print(node.e)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def _generate_depth_string(self, depth):
        res = ''
        for i in range(depth):
            res += '--'
        return res

    def _generate_BST_string(self, node, depth, res):
        if not node:
            res.append(self._generate_depth_string(depth) + 'None\n')
            return
        res.append(self._generate_depth_string(depth) + str(node.e) + '\n')
        self._generate_BST_string(node.left, depth + 1, res)
        self._generate_BST_string(node.right, depth + 1, res)

    def __str__(self):
        res = []
        self._generate_BST_string(self._root, 0, res)
        return '<chapter_06_BST.bst.BST>:\n' + ''.join(res)

    def __repr__(self):
        return self.__str__()
