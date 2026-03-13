class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    current = head

    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev
