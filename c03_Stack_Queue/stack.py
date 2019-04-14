from c02_Array.array import Array
from c03_Stack_Queue.base import StackBase


class ArrayStack(StackBase):
    def __init__(self):
        self._array = Array()

    def push(self, e):
        self._array.add_last(e)

    def pop(self):
        return self._array.remove_last()

    def peak(self):
        return self._array.get_last()

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def __str__(self):
        return str('<chapter_03_Stack_Queue.stack.ArrayStack> : {}'.format(self._array))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    s = ArrayStack()
    for i in range(0, 20):
        s.push(i)
        print(s)

    for i in range(0, 10):
        s.pop()
        print(s)