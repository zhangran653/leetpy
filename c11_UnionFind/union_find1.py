from c11_UnionFind.base import UF


class UnionFind1(UF):

    def __init__(self, size):
        self._id = [i for i in range(0, size)]

    def is_connected(self, p, q):
        return self._id[p] == self._id[q]

    def _find(self, p):
        if p < 0 or p >= len(self._id):
            raise ValueError('p is out of bound.')
        return self._id[p]

    # O(1)
    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    # O(n)
    def union_elements(self, p, q):
        if p < 0 or p >= len(self._id) or q < 0 or q >= len(self._id):
            raise ValueError('Illegal argument.')
        p_id = self._find(p)
        q_id = self._find(q)
        if p_id == q_id:
            return
        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id

    def get_size(self):
        return len(self._id)
