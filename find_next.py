class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.parent = None
def find_next(node):
    if not node.right:
        new_node = node.parent
        if new_node.left==node:
            return new_node
        else:
            new_node = node.parent.parent
            while not new_node.left:
                new_node = new_node.parent
            return new_node
    else:
        new_node = node.right
        while new_node.left:
            new_node = new_node.left 
        return new_node
    return None