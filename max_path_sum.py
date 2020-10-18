class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def max_sub_path(root):
    if root is None:
        return 0
    l = max_sub_path(root.left)
    r = max_sub_path(root.right)
    max_path_through = max(root.data,max(l,r)+root.data,l+r+root.data)
    max_sub_path.res = max(max_path_through,max_sub_path.res)
    return max_path_through
def main(root):
    max_sub_path.res = -float('inf')
    return max_sub_path(root)
root = Node(10) 
root.left = Node(2) 
root.right   = Node(10)
root.left.left  = Node(20) 
root.left.right = Node(1)
root.right.right = Node(-25) 
root.right.right.left   = Node(3)
root.right.right.right  = Node(4)
print("Max path sum is " ,main(root))
    