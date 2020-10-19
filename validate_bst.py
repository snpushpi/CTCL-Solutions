class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def validate_bst(binary_tree):
    if not binary_tree:
        return True
    if not binary_tree.left and not binary_tree.right:
        return True
    if not binary_tree.left:
        return binary_tree.data<=binary_tree.right.data and validate_bst(binary_tree.right)
    if not binary_tree.right:
        return binary_tree.left.data<=binary_tree.data and validate_bst(binary_tree.left)
    return binary_tree.left.data<=binary_tree.data<=binary_tree.right.data and validate_bst(binary_tree.left) and validate_bst(binary_tree.right)