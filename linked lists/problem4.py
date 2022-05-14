# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

def find_intersect(head1, head2):
    n1, n2 = head1, head2 #nodes 1 and 2
    i1 = i2 = None
    while n1 != n2:
        if n1:
            n1 = n1.next
        if n2:
            n2 = n2.next

    return (i1 if (i1 is not None) else i2)