from c06_BST.bst import BST
from c07_Set_Map.base import SetBase


class BSTSet(SetBase):
    def __init__(self):
        self._bst = BST()

    def add(self, e):
        return self._bst.add(e)

    def remove(self, e):
        return self._bst.remove(e)

    def contains(self, e):
        return self._bst.contains(e)

    def get_size(self):
        return self._bst.get_size()

    def is_empty(self):
        return self._bst.is_empty()
