class Array:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._size = 0

    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def add_last(self, e):
        self.add(self._size, e)

    def get_last(self):
        return self.get(self._size - 1)

    def get_first(self):
        return self.get(0)

    def add_first(self, e):
        self.add(0, e)

    def add(self, index, e):

        if not 0 <= index <= self._size:
            raise ValueError('add fail, index should between 0 and size')

        if self._size == len(self._data):
            self._resize(2 * self._size)

        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = e
        self._size += 1

    def __str__(self):
        return str(
            '<chapter_02_Array.array.Array> : {}, capacity: {}'.format(self._data[:self._size], self.get_capacity()))

    def __repr__(self):
        return self.__str__()

    def get(self, index):
        if not 0 <= index < self._size:
            raise ValueError('get failed. Index is illegal.')

        return self._data[index]

    def set(self, index, e):
        if not 0 <= index < self._size:
            raise ValueError('get failed. Index is illegal.')

        self._data[index] = e

    def contains(self, e):
        for i in range(0, self._size):
            if self._data[i] == e:
                return True
        return False

    def find(self, e):
        for i in range(0, self._size):
            if self._data[i] == e:
                return i
        return -1

    def remove(self, index):
        if not 0 <= index < self._size:
            raise ValueError('remove failed. Index is illegal.')
        ret = self._data[index]
        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]
        self._data[self._size - 1] = None
        self._size -= 1

        if self._size == len(self._data) // 4 and len(self._data) // 2 != 0:
            self._resize(len(self._data) // 2)
        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, e):
        index = self.find(e)
        if not index == -1:
            self.remove(index)

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(0, self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def swap(self, i, j):
        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise ValueError('Index is illegal.')
        self._data[i], self._data[j] = self._data[j], self._data[i]


if __name__ == '__main__':
    a = Array(10)
    a.add(0, 1)
    a.add(1, 2)
    a.add(2, 3)
    a.add_last(4)
    a.add_first(0)
    print(a)
    print(a.get(4))
    a.set(4, 6)
    print(a)

    print(a.contains(6))
    print(a.contains(5))
    print(a.find(3))
    print(a.find(5))
    print('--')
    print(a.remove(1))

    print(a)
