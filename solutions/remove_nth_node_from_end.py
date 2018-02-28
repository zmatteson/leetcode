class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(node):
    traverse = True
    while traverse == True:
        print(node.val, " -> ", end="")
        if node.next == None:
            traverse = False
        else:
            node = node.next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    size = find_size(head)
    if size == 1:
        return None
    position = size - n - 1
    if position == -1:
        return head.next
    prev_node = head
    node = prev_node.next
    while position:
        node = node.next
        prev_node = prev_node.next
        position -= 1
    prev_node.next = node.next
    return head


def find_size(head):
    size = 1
    while head.next:
        head = head.next
        size += 1
    return size

if __name__ == "__main__":
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_c = ListNode(3)
    node_a.next = node_b
    node_b.next = node_c
    print("The list is :")
    print_list(node_a)
    print("\nThe list with node", 3, " from end removed is: ")
    node_a = removeNthFromEnd(node_a, 3)
    print_list(node_a)

    node_a = ListNode(1)
    node_b = ListNode(2)
    node_c = ListNode(3)
    node_a.next = node_b
    node_b.next = node_c
    print("The list is :")
    print_list(node_a)
    print("\nThe list with node", 2, " from end removed is: ")
    node_a = removeNthFromEnd(node_a, 2)
    print_list(node_a)

    node_a = ListNode(1)
    node_b = ListNode(2)
    node_c = ListNode(3)
    node_a.next = node_b
    node_b.next = node_c
    print("The list is :")
    print_list(node_a)
    print("\nThe list with node", 1, " from end removed is: ")
    node_a = removeNthFromEnd(node_a, 1)
    print_list(node_a)
