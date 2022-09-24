class Heap(object):
    def __init__(self):
        self.items = []
        self.size = 0

    def insert(self, item):
        self.size += 1
        self.items[self.size] = item

        current = self.size
        while self.items[current] < self.items[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    @staticmethod
    def _parent(pos):
        return pos // 2

    @staticmethod
    def _left_child(pos):
        return pos * 2

    @staticmethod
    def _right_child(pos):
        return (pos * 2) + 1

    def _is_leaf(self, pos):
        return (pos * 2) > self.size

    def _swap(self, first, second):
        self.items[first], self.items[second] = self.items[second], self.items[first]

    def min_heapify(self, pos):
        if not self._is_leaf(pos):
            if self._left_child(pos) < self.items[pos] or self._right_child(pos) < self.items[pos]:
                if self._left_child(pos) < self._right_child(pos):
                    self._swap(pos, self._left_child(pos))
                    self.min_heapify(self._left_child(pos))
                else:
                    if self._right_child(pos) < self._left_child(pos):
                        self._swap(pos, self._right_child(pos))
                        self.min_heapify(self._right_child(pos))

    def remove(self, item):
        pass
