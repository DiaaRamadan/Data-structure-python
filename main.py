from linkedlist.iscircular import is_circular
from linkedlist.linked_list import LinkedList

linkedlist = LinkedList()
linkedlist.append(10)
linkedlist.append(15)
linkedlist.append(8)
linkedlist.append(30)
linkedlist.append(20)
linkedlist.insert(40, 40)

print(is_circular(linkedlist.head))

print(linkedlist.to_list())
