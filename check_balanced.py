def check_balanced(root):
    if not root:
        return (True,0)
    left_balanced, left_depth = check_balanced(root.left)
    if not left_balanced:
        return (False,0)
    right_balanaced, right_depth = check_balanced(root.right)
    if not right_balanaced and abs(left_depth-right_depth)>1:
        return (False,0)
    return (True,max(left_depth,right_depth)+1)
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None