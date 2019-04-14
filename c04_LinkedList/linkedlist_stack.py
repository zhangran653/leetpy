from c03_Stack_Queue.base import StackBase
from c04_LinkedList.linkedlist import LinkedList


class LinkedListStack(StackBase):
    def __init__(self):
        self._list = LinkedList()

    def __str__(self):
        curr = self._list._dummy_head.next
        data = []
        while curr:
            data.append(str(curr.e))
            curr = curr.next
        return '<chapter_03_LinkedList.linkedlist_stack.LinkedListStack>: (Top) ' + ' -> '.join(data)

    def __repr__(self):
        return self.__str__()

    def push(self, e):
        self._list.add_last(e)

    def pop(self):
        return self._list.remove_first()

    def peak(self):
        return self._list.get_first()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()
