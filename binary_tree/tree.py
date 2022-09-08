class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_right_child(self):
        return self.right

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def set_left_child(self, node):
        self.left = node

    def has_right_child(self):
        return self.right is not None

    def has_left_child(self):
        return self.left is not None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree:
    def __init__(self):
        self._root = None

    def get_root(self):
        return self._root

    def insert(self, value):
        node = Node(value)
        if self._root is None:
            self._root = node
            return
        current = self._root
        while True:
            if value < current.get_value():
                if not current.has_left_child():
                    current.set_left_child(node)
                    break
                current = current.get_left_child()
            else:
                if not current.has_right_child():
                    current.set_right_child(node)
                    break
                current = current.get_right_child()

    @staticmethod
    def _is_leaf(node):
        return not node.has_right_child and not node.has_left_child()

    def search(self, value):
        current = self._root
        while current is not None:
            if value == current.get_value():
                return True
            elif value < current.get_value():
                current = current.get_left_child()
            else:
                current = current.get_right_child()
        return False

    def pre_order_traverse(self) -> list:
        nodes = []
        self._pre_order_traverse(self._root, nodes)
        return nodes

    def _pre_order_traverse(self, node, list_of_nodes: list):
        if node is None:
            return None
        list_of_nodes.append(self._root.get_value())
        self._pre_order_traverse(node.get_left_child(), list_of_nodes)
        self._pre_order_traverse(node.get_right_child(), list_of_nodes)

    def in_order_traverse(self) -> list:
        nodes = []
        self._in_order_traverse(self._root, nodes)
        return nodes

    def _in_order_traverse(self, node, list_of_nodes: list):
        if node is None:
            return None
        self._pre_order_traverse(node.get_left_child(), list_of_nodes)
        list_of_nodes.append(self._root.get_value())
        self._pre_order_traverse(node.get_right_child(), list_of_nodes)

    def post_order_traverse(self) -> list:
        nodes = []
        self._post_order_traverse(self._root, nodes)
        return nodes

    def _post_order_traverse(self, node, list_of_nodes: list):
        if node is None:
            return None
        self._post_order_traverse(node.get_left_child(), list_of_nodes)
        self._post_order_traverse(node.get_right_child(), list_of_nodes)
        list_of_nodes.append(self._root.get_value())

    def get_depth(self):
        return self._get_depth(self._root)

    def _get_depth(self, root: Node):
        if root is None:
            return -1
        if self._is_leaf(root):
            return 0
        return max(self._get_depth(root.get_right_child()), self._get_depth(root.get_left_child())) + 1

    def delete(self, value):
        self._delete(self._root, value)

    def _delete(self, root: Node, value):
        if root is None:
            return
        if root.get_value() > value:
            root.set_left_child(self._delete(root.get_left_child(), value))
        elif root.get_value() < value:
            root.set_right_child(self._delete(root.get_right_child(), value))
        else:
            if root.get_left_child() is None:
                temp = root.get_right_child()
                root = None
                return temp
            elif root.get_right_child() is None:
                temp = root.get_left_child()
                root = None
                return temp

            min_child = self._find_min(root)
            root.set_value(min_child.get_value())

            root.set_right_child(self._delete(root.get_right_child(), min_child.get_value()))
            return root

    @staticmethod
    def _find_min(root: Node):
        current = root
        while current.get_left_child() is not None:
            current = current.get_left_child
        return current


tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(6)
tree.insert(4)
tree.insert(2)

print(tree.get_depth())
