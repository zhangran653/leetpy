class StackBase:
    def push(self, e):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peak(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError


class QueueBase:

    def enqueue(self, e):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def get_front(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError
