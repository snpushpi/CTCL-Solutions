def kth_to_last(head,k):
    lead, follow = head, head
    for i in range(k):
        if not lead:
            return None
        lead = lead.next
    while lead:
        lead, follow = lead.next, follow.next
    return follow
class Node():
    def __init__(self,data,next):
        self.data = data
        self.next = next
