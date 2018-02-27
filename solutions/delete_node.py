"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

Supposing that we are given the position, we have to traverse the array
Given 2 as the 2nd node, we would delete 2 in 1 -> 2 -> 3
We do not consider the case where we delete the last node
Assumptions:  the value x is in the linked list
		We have access to this node!
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Method 1:
copy the next node over
"""
def print_list(node):
    traverse = True
    while traverse == True:
        print(node.val, " -> ", end="")
        if node.next == None:
            traverse = False
        else:
            node = node.next

def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
        

if __name__ == "__main__":
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_c = ListNode(3)
    node_d = ListNode(4)
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    print("The linked list is")
    print_list(node_a)
    deleteNode(node_a)
    print("\nThe list with node_a removed is")
    print_list(node_a)

    node_a = ListNode(1)
    node_b = ListNode(2)
    node_a.next = node_b
    print("The linked list is")
    print_list(node_a)
    deleteNode(node_a)
    print("\nThe list with node_a removed is")
    print_list(node_a)

"""
Given 1 -> 2 we expect 2 ->
"""

        

