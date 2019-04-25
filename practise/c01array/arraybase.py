class ArrayBase:
    def get_size(self):
        raise NotImplementedError

    def get_capacity(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def add_last(self, e):
        raise NotImplementedError

    def get_last(self):
        raise NotImplementedError

    def get_first(self):
        raise NotImplementedError

    def add_first(self, e):
        raise NotImplementedError

    def add(self, index, e):
        raise NotImplementedError

    def get(self, index):
        raise NotImplementedError

    def set(self, index, e):
        raise NotImplementedError

    def contains(self, e):
        raise NotImplementedError

    def find(self, e):
        raise NotImplementedError

    def remove(self, index):
        raise NotImplementedError

    def remove_first(self):
        raise NotImplementedError

    def remove_last(self):
        raise NotImplementedError

    def remove_element(self, e):
        raise NotImplementedError

    def _resize(self, new_capacity):
        raise NotImplementedError

    def swap(self, i, j):
        raise NotImplementedError
