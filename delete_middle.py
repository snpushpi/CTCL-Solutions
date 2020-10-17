def delete_middle(node):
    next = node.next
    node.data = next.data
    node.next = next.next
    