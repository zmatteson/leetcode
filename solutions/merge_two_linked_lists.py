"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

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

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    node_a = l1  # 1 -> 2 -> 3
    node_b = l2  # 4 -> 5 -> 6

    if l1 == None:
        if l2 == None:
            return None
        else:
            return l2
    if l2 == None:
        return l1
    if l1.next == None and l2.next == None:
        l2.next = l1
        return l2

    while node_a.next and node_b.next:  # 1 -> 4 -> 2 -> 5 -> 3
        copy_a = node_a  # 2 -> 3
        copy_b = node_b  # 5 -> 6

        node_a = node_a.next  # 3 ->
        node_b = node_b.next  # 6 ->

        copy_a.next = copy_b  # 2 -> 5
        copy_b.next = node_a  # 5 -> 3

    if node_a.next != None:
        copy_a = node_a
        node_a.next = node_b
        node_b.next = copy_a.next
    else:
        node_a.next = node_b

    return l1

if __name__ == "__main__":
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_c = ListNode(3)
    node_d = ListNode(4)
    node_e = ListNode(5)
    node_f = ListNode(6)
    node_a.next = node_b
    node_b.next = node_c
    node_d.next = node_e 
    node_e.next = node_f

    print("The lists are :")
    print_list(node_a)
    print()
    print_list(node_d)

    print("\nThe list merged is: ")
    node_a = mergeTwoLists(node_a, node_d)
    print_list(node_a)

    node_a = ListNode(1)
    node_d = ListNode(4)
    print("The lists are :")
    print_list(node_a)
    print()
    print_list(node_d)

    print("\nThe list merged is: ")
    node_a = mergeTwoLists(node_a, node_d)
    print_list(node_a)