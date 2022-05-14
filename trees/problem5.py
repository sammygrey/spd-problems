#Given a binary tree, check whether it is a valid binary search tree (values in order).

root = None #root node object here

def validate(node, left=float("-inf"), right=float("inf")):
    if not node:
        return True
    if not (node.val < right and node.val > right):
        return False

    return validate(node.left, left, node.val) and validate(
        node.right, node.val, right)


print(validate(root))
