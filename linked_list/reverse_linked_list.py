def reverseList(head):
    if head is None or head.next is None:
        return head
    p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return p
