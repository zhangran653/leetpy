from c03_Stack_Queue.base import QueueBase


class LoopQueue(QueueBase):
    def __init__(self, capacity=10):
        self._data = [None] * (capacity + 1)
        self._size, self._front, self._tail = 0, 0, 0

    def is_empty(self):
        return self._front == self._tail

    def get_size(self):
        return self._size

    def enqueue(self, e):
        if (self._tail + 1) % self._data.__len__() == self._front:
            self.resize(self._size * 2)
        self._data[self._tail] = e
        self._tail = (self._tail + 1) % self._data.__len__()
        self._size += 1

    def dequeue(self):
        d = self._data[self._front]
        self._front = (self._front + 1) % self._data.__len__()
        self._size -= 1
        if self._size == self._data.__len__() // 4 and self._data.__len__() // 2 != 0:
            self.resize(self._data.__len__() // 2)
        return d

    def get_front(self):
        return self._data[self._front]

    def resize(self, new_capacity):
        new_data = [None] * (new_capacity + 1)
        for i in range(0, self._size):
            new_data[i] = self._data[(self._front + i) % self._data.__len__()]
        self._data = new_data
        self._front, self._tail = 0, self._size

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        r = 'Front ['
        for i in range(0, self._size):
            r += str(self._data[(self._front + i) % self._data.__len__()]) + ' '
        r += '] Tail'
        return r


if __name__ == '__main__':
    print(11)
    s = LoopQueue(10)
    for i in range(0, 20):
        s.enqueue(i)
        print(s)

    for i in range(0, 10):
        print(s.dequeue())
        print(s)
