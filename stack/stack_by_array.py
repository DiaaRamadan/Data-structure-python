class Stack:
    def __init__(self, initial_size):
        self._current_index = 0
        self._num_elements = 0
        self._elements = [0 for _ in range(initial_size)]

    def push(self, data):
        if self._num_elements >= len(self._elements):
            self._handle_stack_capacity_full()
        self._elements[self._current_index] = data
        self._num_elements += 1
        self._current_index += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self._current_index -= 1
        self._num_elements -= 1
        item = self._elements[self._current_index]
        return item

    def is_empty(self):
        return self._num_elements == 0

    def _is_full(self):
        return self._num_elements == len(self._elements)

    def size(self):
        return self._num_elements

    def _handle_stack_capacity_full(self):
        old_elements = self._elements
        self._elements = [0 for _ in range(2 * len(old_elements))]
        for index, value in enumerate(old_elements):
            self._elements[index] = value


# stack = Stack(10)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.push(6)
# stack.push(7)
# stack.push(8)
# stack.push(9)
# stack.push(10)
# stack.push(11)
#
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print("---------------------")
# print(stack.size())
