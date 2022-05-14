# Given a singly-linked list, find whether or not it contains a cycle, and if it does, find the node at which the cycle starts (the node that two other nodes reference/point to).

def detect_cycle(head): #another use for two pointer 
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False