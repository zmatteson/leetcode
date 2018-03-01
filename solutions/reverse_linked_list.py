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


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # Check base case:
    if head == None:
        return None
    elif head.next == None:
        return head
    else:
        node = head.next  # node = 2 -> 3
        prev_node = head
        prev_node.next = None
        node_copy = node
        while node:
            node_copy = node
            node = node.next
            node_copy.next = prev_node
            prev_node = node_copy
        return node_copy


if __name__ == "__main__":
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_c = ListNode(3)
    node_a.next = node_b
    node_b.next = node_c
    print("The list is :")
    print_list(node_a)
    print("\nThe list reversed is: ")
    node_a = reverseList(node_a)
    print_list(node_a)
