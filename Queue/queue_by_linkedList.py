from linkedlist.linked_list import LinkedList


class Queue:
    def __init__(self):
        self._queue = LinkedList()

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        return self._queue.pop()

    def is_empty(self):
        return self._queue.size() == 0

    def size(self):
        return self._queue.size()


queue = Queue()
queue.enqueue(10)
queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13)
print(queue.dequeue())
