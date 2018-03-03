

def isPalindrome(head):
    """

    :type head: ListNode

    :rtype: bool

    """

    if not head or not head.next:

        return True

    length = find_length(head)

    l1, l2 = split_and_reverse(head, length//2)

    if length % 2 != 0:

        l2 = l2.next

    for _ in range(length//2):

        if l1.val != l2.val:

            return False

        l1 = l1.next

        l2 = l2.next

    return True


def split_and_reverse(head, n):

    new_head = None

    while n:

        copy = head

        head = copy.next

        copy.next = new_head

        new_head = copy

        n -= 1

    return new_head, head


def find_length(head):

    count = 0

    if head:

        while head:

            count += 1

            head = head.next

    return count
