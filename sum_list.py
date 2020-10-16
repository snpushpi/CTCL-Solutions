class Node():
    def __init__(self,data,next):
        self.data = data
        self.next = next
def sum_list(num1, num2):
    node1, node2 = num1, num2
    result_head, result_node = None, None
    carry = 0
    while node1 or node2:
        value = 0
        if node1:
            value += node1.data
            node1 = node1.next 
        if node2:
            value+=node2.data 
            node2 = node2.next
        value+=carry
        node = Node(value%10)
        carry = value//10
        if result_node:
            result_node.next = node
            result_node = node
        else:
            result_head = node
            result_node = node
    return result_head


