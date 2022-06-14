from linkedlist.linked_list import LinkedList, Node


class Stack:
    def __init__(self):
        self._num_elements = 0
        self.head = None

    def push(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self._num_elements += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self.head.value
        self.head = self.head.next
        self._num_elements -= 1
        return item

    def size(self):
        return self._num_elements

    def is_empty(self):
        return self.head is None


# stack = Stack()
# print(stack.is_empty())
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
# print(stack.size())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print("size = " + str(stack.size()))
# print(stack.is_empty())
