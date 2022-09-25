import sys


class Heap(object):
    def __init__(self, max_size):
        self._max_size = max_size
        self._items = [0] * (self._max_size + 1)
        self._items[0] = -1 * sys.maxsize
        self._size = 0
        self._front = 1

    def insert(self, item):
        if self.is_full():
            raise Exception("Heap Full")
        self._size += 1
        self._items[self._size] = item

        current = self._size
        while self._items[current] < self._items[self._parent(current)]:
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
        return (pos * 2) > self._size

    def _swap(self, first, second):
        self._items[first], self._items[second] = self._items[second], self._items[first]

    def min_heapify(self, pos):
        if not self._is_leaf(pos):
            if self._left_child(pos) < self._items[pos] or self._right_child(pos) < self._items[pos]:
                if self._left_child(pos) < self._right_child(pos):
                    self._swap(pos, self._left_child(pos))
                    self.min_heapify(self._left_child(pos))
                else:
                    if self._right_child(pos) < self._left_child(pos):
                        self._swap(pos, self._right_child(pos))
                        self.min_heapify(self._right_child(pos))

    def remove(self):
        if self.is_empty():
            raise Exception("Empty heap")

        removed_item = self._items[self._front]
        self._items[self._front] = self._items[self._size]
        self._items[self._size] = 0
        self._size -= 1
        self.min_heapify(self._front)
        return removed_item

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size >= self._max_size

    def display(self):
        for i in range(1, (self._size // 2) + 1):
            print(" PARENT : " + str(self._items[i]) + " LEFT CHILD : " +
                  str(self._items[2 * i]) + " RIGHT CHILD : " +
                  str(self._items[2 * i + 1]))


heap = Heap(20)
heap.insert(5)
heap.insert(10)
heap.insert(1)
heap.insert(3)
heap.insert(11)
heap.insert(2)
# heap.remove()

heap.display()
