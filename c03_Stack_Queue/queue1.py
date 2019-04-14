from c02_Array.array import Array
from c03_Stack_Queue.base import QueueBase


class ArrayQueue(QueueBase):
    def __init__(self):
        self._array = Array()

    def enqueue(self, e):
        return self._array.add_last(e)

    def dequeue(self):
        return self._array.remove_first()

    def get_front(self):
        return self._array.get_first()

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def __str__(self):
        return str('<chapter_03_Stack_Queue.stack.ArrayQueue> : {}'.format(self._array))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    s = ArrayQueue()
    for i in range(0, 20):
        s.enqueue(i)
        print(s)

    for i in range(0, 10):
        s.dequeue()
        print(s)
