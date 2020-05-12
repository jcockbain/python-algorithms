from Node import Node


def add_two_numbers(l1, l2):
    carry = 0
    dummyHead = Node(0)
    res = dummyHead
    while l1 or l2:
        x = 0 if l1 is None else l1.val
        y = 0 if l2 is None else l2.val
        s = carry + x + y
        carry = s // 10
        res.next = Node(s % 10)
        res = res.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
    if carry > 0:
        res.next = Node(carry)
    return dummyHead.next
