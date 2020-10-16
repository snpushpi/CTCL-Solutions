def kth_from_last(head,k):
    lead, follow = head, head
    for i in range(k):
        if lead:
            lead = lead.next
        else:
            return None
    while lead:
        lead, follow = lead.next, follow.next
    return follow