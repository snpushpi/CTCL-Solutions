class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def minimal_height_bst(list1):
    if len(list1)==0:
        return None
    if len(list1)==1:
        return Node(list1[0])
    middle = len(l)//2
    node = Node(list1[middle])
    l = minimal_height_bst([:middle])
    r = minimal_height_bst([middle+1:])
    node.left = l
    node.right = r
    return node
