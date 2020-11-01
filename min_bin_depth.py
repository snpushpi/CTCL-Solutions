class Node():
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
def min_depth(node):
    if not node:
        return 0
    if not node.left or not node.right:
        return 1
    if not node.left:
        return min_depth(node.right)+1
    if not node.right:
        return min_depth(node.left)+1
    return min(min_depth(node.left)+1,min_depth(node.right)+1)