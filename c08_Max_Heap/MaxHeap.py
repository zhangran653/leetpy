from c02_Array.array import Array


class MaxHeap:
    def __init__(self, capacity=None):
        if not capacity:
            self._data = Array()
        else:
            self._data = Array(capacity=capacity)

    def size(self):
        return self._data.get_size()

    def is_empty(self):
        return self._data.is_empty()

    # 返回完全二叉树数组表示中，一个索引所表示的元素的父亲节点的索引 i // 2
    def _parent(self, index):
        if index == 0:
            raise ValueError('index-0 doesn\'t have parent.')
        return (index - 1) // 2

    # 返回完全二叉树数组表示中，一个索引所表示的元素的左孩子节点的索引 2 * i + 1
    def _left_child(self, index):
        return index * 2 + 1

    # 返回完全二叉树数组表示中，一个索引所表示的元素的右孩子节点的索引 2 * i + 2
    def _right_child(self, index):
        return index * 2 + 2

    def add(self, e):
        self._data.add_last(e)
        self._sift_up(self._data.get_size() - 1)

    def _sift_up(self, index):
        while index > 0 and self._data.get(index) > self._data.get(self._parent(index)):
            self._data.swap(index, self._parent(index))
            index = self._parent(index)

    def extract_max(self):
        e = self.find_max()
        self._data.swap(0, self._data.get_size() - 1)
        self._data.remove_last()
        self._sift_down()
        return e

    def find_max(self):
        if self._data.get_size() == 0:
            raise ValueError('Can not find_max when heap is empty.')
        return self._data.get(0)

    def _sift_down(self, k):
        while self._left_child(k) < self._data.get_size():
            j = self._left_child(k)
            if j + 1 < self._data.get_size() and self._data.get(j + 1) > self._data.get(j):
                # 说明右孩子的值比左孩子的值大
                j = self._right_child(k)
            # 此时self._data.get(j)是左孩子和右孩子中的最大值
            if self._data.get(k) > self._data.get(j):
                break
            self._data.swap(k, j)
            k = j


if __name__ == '__main__':
    n = 1000
    from time import time

    start_time1 = time()
    max_heap = MaxHeap()
    from random import randint

    for i in range(n):
        max_heap.add(randint(0, 1000))
    print('heap add: ', time() - start_time1)  # head add:  5.748132228851318
