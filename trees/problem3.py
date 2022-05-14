#Given a binary tree containing numbers, 
#find the maximum sum path (the path that has the largest sum of node values). 
#The path may start and end at any node in the tree.

max_sum = None
root = None #root node object here

def find_max_sum(node):
    global max_sum
    if node is None:
        return 0
    
    left = find_max_sum(node.left)
    right = find_max_sum(node.right)

    current_max = max(max(left, right) + root.data, root.data)

    earlier_max = max(current_max, left + right + root.data)

    max_sum = max(max_sum, earlier_max)

    return max_sum

print(find_max_sum(root))