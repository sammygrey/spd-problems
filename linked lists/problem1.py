#Given a single-linked list, find the middle value in the list.

def find_mid(head): #simple two pointer approach to finding middle of linked list
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

