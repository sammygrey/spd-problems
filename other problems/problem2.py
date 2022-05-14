#Given a binary search tree, convert it into a sorted doubly-linked list 
#by modifying the original tree nodes (do not create new nodes).
head, tail = None, None

def dfs(node): #simple depth first search for binary search trees
    global head, tail
    if node is None: #node.left or node.right can be None, so check first because recursive calls
        return
    dfs(node.left) 
    if tail:
        tail.right = node #right and left are uncommon in linked lists for nodes, but super common for bst nodes, so we use these
        node.left = tail
    else:
        head = node
    tail = node
    dfs(node.right)

def bst_to_dlinked(root):
    dfs(root)
    head.left = tail #finally, connect head and tail
    tail.right = head

    return head