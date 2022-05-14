# Given an array of k singly-linked lists, each of whose values are in sorted order,
# combine all nodes (do not create new nodes) into one singly-linked list with all values in order.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sorted_merge(l1,l2):
    new_list = Node()#list intiializer here or just a node I don't judge
    tail = new_list#list.tail or node

    if l2 is None: #just to speed up the process, we dont want to recreate the list part by part
        return l1

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

def merge_lists(lists): #basically just merge 2 at a time (keep one the same if uneven number)
    for i in range(len(lists), 2):
        l1 = lists[i]
        del lists[i]
        l2 = None
        if (i + 1) < len(lists):
            l2 = lists[i + 1]
            del lists[i+1]
        lists.append(sorted_merge(l1, l2)) #end of the day doesnt matter if this is prepended or appended, this will be kept the same as l1 if l2 is None