# Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sorted_merge(l1,l2):
    new_list = Node()#list intiializer here or just a node I don't judge
    tail = new_list#list.tail or node

    c1, c2 = l1.head, l2.head #current nodes 1 and 2

    while c1 or c2:
        if c1:
            tail.next = Node(c1.value, None) #data, next -> set as next tail just incase, may be no c2 to compare to so preset
            if c2:
                if c1.data > c2.data:
                    tail.next = Node(c2.value, None)
                    c2 = c2.next
                else:
                    c1 = c1.next
            else: 
                c1 = c1.next
        elif c2: #if no c1 to compare
            tail.next = Node(c2.value, None)
            c2 = c2.next
        tail = tail.next #reassign tail to new last element
    return new_list