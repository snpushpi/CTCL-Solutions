class Node():
    def __init__(self,data,next):
        self.data = data
        self.next = next
def remove_duplicates(head):
    node = head
    if node:
        values = {node.data:True}
        while node.next:
            if node.next in values:
                node.next = node.next.next
            else:
                values[node.next.data]=True
                node = node.next
    return head