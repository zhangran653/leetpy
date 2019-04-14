class LinkedList:
    class _Node:
        def __init__(self, e=None, next_node=None):
            self.e = e
            self.next = next_node

        def __str__(self):
            return str(self.e)

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def add(self, index, e):
        if index < 0 or index > self._size:
            raise ValueError('index should between 0 and size')

        pre = self._dummy_head
        for i in range(0, index):
            pre = pre.next
        pre.next = self._Node(e, pre.next)
        self._size += 1

    def add_first(self, e):
        self.add(0, e)

    def add_last(self, e):
        self.add(self._size, e)

    def getter(self, index):
        if index < 0 or index > self._size:
            raise ValueError('index should between 0 and size')
        cur = self._dummy_head.next
        for i in range(0, index):
            cur = cur.next
        return cur

    def get_first(self):
        return self.getter(0)

    def get_last(self):
        return self.getter(self._size - 1)

    def setter(self, index, e):
        if index < 0 or index > self._size:
            raise ValueError('index should between 0 and size')
        cur = self._dummy_head.next
        for i in range(0, index):
            cur = cur.next
        cur.e = e

    def remove(self, index):
        if index < 0 or index > self._size:
            raise ValueError('index should between 0 and size')

        pre = self._dummy_head
        for i in range(0, index):
            pre = pre.next
        ret = pre.next
        pre.next = ret.next
        ret.next = None
        self._size -= 1
        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def contains(self, e):
        cur = self._dummy_head.next
        while cur:
            if cur.e == e:
                return True
            cur = cur.next
        return False

    def __str__(self):
        curr = self._dummy_head.next
        data = []
        while curr:
            data.append(str(curr.e))
            curr = curr.next
        return '<chapter_03_LinkedList.linkedlist.LinkedList>: (Head) ' + \
               ' -> '.join(data) + ' (Tail)'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    l = LinkedList()
    l.add_first(0)
    l.add_first(1)
    print(l)

    l.add_last(6)
    l.add_last(7)
    print(l)

    l.add(2, 8)
    print(l)

    print(l.get_last())
    print(l.get_first())
    print(l.getter(3))

    l.setter(3, 666)
    l.setter(0, 111)
    l.setter(l.get_size() - 1, 999)
    print(l)

    print(l.remove_first())
    print(l.remove_last())
    print(l.remove(1))

    print(l)

    print(l.contains(1))
    print(l.contains(0))
    print(l.contains(666))

    print(l.is_empty())
    print(l.get_size())
