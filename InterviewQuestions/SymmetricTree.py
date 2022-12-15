#  Given a binary tree `root`, check if it's symmetric around its center (mirrors itself)

# For tree problems, solution is normally recursive

# Helper Function
def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)

# O(n) Time Complexity, just a Depth First Search
# O(logn) Space Complexity, Binary Tree
def tree_is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)

# def tree_sum(root):
#     if root is None:
#         return 0
#     else:
#         left_sum = tree_sum(root.left)
#         right_sum = tree_sum(root.right)
#         return root.val + left_sum + right_sum