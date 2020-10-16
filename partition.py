def partition(head, pivot):
    a_head,a_tail = None, None
    b_head, b_tail = None, None
    node = head
    while node:
        if node.data<pivot:
            if a_head:
                a_tail.next = node
                a_tail = node
            else:
                a_head, a_tail = node, node 
        else:
            if b_head:
                b_tail.next = node
                b_tail = node
            else:
                b_head, b_tail = node, node 
        node = node.next

    