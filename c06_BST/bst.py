from collections import deque


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

    def pre_order_nr(self):
        stack = []
        stack.append(self._root)
        while stack:
            cur = stack.pop()
            print(cur)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    def in_order(self):
        self._in_order(self._root)

    def _in_order(self, node):
        if not node:
            return
        self._in_order(node.left)
        print(node.e)
        self._in_order(node.right)

    def post_order(self):
        self._post_order(self._root)

    def _post_order(self, node):
        if not node:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.e)

    def level_order(self):
        queue = deque()
        queue.append(self._root)
        while queue:
            cur = queue.popleft()
            print(cur)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    def minimum(self):
        if self._size == 0:
            raise ValueError('BST empty')
        return self._minimum(self._root)

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def maximum(self):
        if self._size == 0:
            raise ValueError('BST empty')
        return self._maximum(self._root)

    def _maximum(self, node):
        if not node.right:
            return node
        return self._maximum(node.right)

    def remove_min(self):
        ret = self.minimum()
        self._root = self._remove_min(self._root)
        return ret

    def _remove_min(self, node):
        if not node.left:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node

        node.left = self._remove_min(node.left)
        return node

    def remove_max(self):
        ret = self.maximum()
        self._root = self._remove_max(self._root)
        return ret

    def _remove_max(self, node):
        if not node.right:
            left_node = node.left
            node.left = None
            self._size -= 1
            return left_node

        node.right = self._remove_max(node.right)
        return node

    def remove(self, e):
        self._remove(self._root, e)

    def _remove(self, node, e):
        if not node:
            return None
        if node.e > e:
            node.left = self._remove(node.left, e)
            self._size -= 1
            return node
        if node.e < e:
            node.right = self._remove(node.right, e)
            self._size -= 1
            return node
        else:
            if not node.left:
                right_node = node.right
                node.right = None
                self._size -= 1
                return right_node
            elif not node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                return left_node
            else:

                successor = self.minimum(node.right)
                successor.right = self._remove_min(node.right)
                successor.left = node.left
                node.left, node.right = None
                return node

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
