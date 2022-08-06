class Queue:
    def __init__(self, initial_size: int):
        self._elements = [0 for _ in range(initial_size)]
        self._size = 0
        self._front = -1
        self._next = 0

    def enqueue(self, value) -> None:
        if self._is_full():
            raise Exception("queue is empty")
        self._elements[self._next] = value
        self._size += 1
        self._next = (self._next + 1) % len(self._elements)
        if self._front == -1:
            self._front = 0

    def dequeue(self):
        if self.is_empty():
            self._front = -1
            return None
        value = self._elements[self._front]
        self._front = (self._front + 1) % len(self._elements)
        self._size -= 1
        return value

    def size(self):
        return self._size

    def _is_full(self) -> bool:
        return len(self._elements) == self._size

    def is_empty(self) -> bool:
        return self._size == 0


queue = Queue(10)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.size())

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

print(queue.size())

