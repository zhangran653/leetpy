class Trie:
    class _Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = dict()

    def __init__(self):
        self._root = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, word):
        cur = self._root
        for w in word:
            if not cur.next.get(w):
                cur.next[w] = self._Node()
            cur = cur.next.get(w)
        if not cur.is_word:
            cur.is_word = True
            self._size += 1

    def contains(self, word):
        cur = self._root
        for w in word:
            if not cur.next.get(w):
                return False
            cur = cur.next.get(w)
        return cur.is_word

    def is_prefix(self, prefix):
        cur = self._root
        for p in prefix:
            if not cur.next.get(p):
                return False
            cur = cur.next.get(p)

        return True


if __name__ == '__main__':
    t = Trie()
    t.add('adf')
    t.add('afeg')
    t.add('adf')
    print(t.get_size())
    print(t.contains('a'))
    print(t.contains('adf'))
    print(t.contains('adfg'))
