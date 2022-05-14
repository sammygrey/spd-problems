# Binary Tree In-order-traversal

result = []
root = None #root node object here

def traverse(node):
    if not node:
        return
    traverse(node.left)
    result.append(node.val)
    traverse(node.right)

traverse(root)
print(result)
