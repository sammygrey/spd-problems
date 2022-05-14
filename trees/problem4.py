#Let's say a binary tree is "super balanced" if the difference between the depths of any two leaf nodes is at most one. 
#Write a function to check if a binary tree is "super balanced"

root = None #root node object here

def is_super_balanced(root):
    if not root:
        return True
    left, right = is_super_balanced(root.left), is_super_balanced(root.right)
    balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
    return balanced

print(is_super_balanced(root))