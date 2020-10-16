def remove_duplicate(head):
    node = head
    node_values = set()
    if node:
        while node.next:
            if node.next.data in node_values:
                node.next = node.next.next
            else:
                node_values.add(node.next.data)
                node  = node.next
    return head
class Node():
    def __init__(self,data,next):
        self.data = data
        self.next = next