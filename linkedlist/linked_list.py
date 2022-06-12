class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Add in first of linked list """
        node = Node(value)
        node.next = self.head
        self.head = node
        return self.head

    def append(self, value):
        """ Add in end of linkedlist """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while True:
                if current.next is None:
                    current.next = node
                    break
                current = current.next
        return self.head

    def search(self, value):
        """ search about specific node by node value"""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def remove(self, value):
        """ Remove node from linkedlist """
        if self.head is None:
            return None

        if self.head.value == value:
            self.head = self.head.next
            return self.head

        current = self.head
        prev = self.head
        while current:
            if current.value == value:
                prev.next = current.next
                return self.head
            prev = current
            current = current.next
        return None

    def pop(self):
        """ Return the first node and Remove it from list """
        if self.head is None:
            return None
        self.head = self.head.next
        return self.head

    def insert(self, value, pos):
        """ insert node in specific pos, If pos is larger than length node will append to the end"""
        node = Node(value)
        if pos == 0:
            node.next = self.head
            self.head = node
            return self.head

        i = 0
        current = self.head
        prev = self.head
        while current:
            if i == pos:
                node.next = current
                prev.next = node
                return self.head
            prev = current
            current = current.next
            i += 1
        prev.next = node
        return self.head

    def size(self):
        """ calculate the length of linkedlist elements """
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def to_list(self):
        """ Convert linkedlist to normal list """
        list_ele = []
        current = self.head
        while current:
            list_ele.append(current.value)
            current = current.next
        return list_ele


linkedlist = LinkedList()
linkedlist.append(10)
linkedlist.append(15)
linkedlist.append(8)
linkedlist.append(30)
linkedlist.append(20)
linkedlist.insert(40, 40)

print(linkedlist.to_list())

