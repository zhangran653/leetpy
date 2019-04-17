from c11_UnionFind.base import UF


class UnionFind2(UF):

    def __init__(self, size):
        self._parent = [i for i in range(0, size)]

    def _find(self, p):
        if p < 0 or p >= len(self._parent):
            raise ValueError('p is out of bound.')
        while self._parent[p] != p:
            p = self._parent[p]

        return p

    # O(1)
    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    # O(n)
    def union_elements(self, p, q):
        if p < 0 or p >= len(self._parent) or q < 0 or q >= len(self._parent):
            raise ValueError('Illegal argument.')
        p_root = self._find(p)
        q_root = self._find(q)

        if q_root == p_root:
            return
        self._parent[p_root] = q_root

    def get_size(self):
        return len(self._parent)
