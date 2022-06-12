from linkedlist.linked_list import Node


def is_circular(head: Node):
    """
    check if linkedlist has circular

    :param head:
    :return: boolean
    """
    if not head:
        return False
    slow = head
    faster = head
    while slow.next and faster.next.next:
        slow = slow.next
        faster = faster.next.next
        if slow == faster:
            return True
    return False
