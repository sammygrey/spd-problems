#Given a binary search tree containing integers and a target integer, 
#come up with an efficient way to locate two nodes in the tree 
#whose sum is equal to the target value.

lookup = set()
k = 0 #value you are looking for here
root = None #bst root node object here

def two_sum_dfs(node):
    global lookup, k

    if node is None:
        return False

    y = k - node.val

    if y in lookup:
        return True
    else:
        lookup.add(node.val)
        
    return two_sum_dfs(node.left) or two_sum_dfs(node.right)


print(two_sum_dfs(root))