# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or k == 0:
            return head

        ll_len = 0
        head_origin = tail_origin = head
        while head:
            ll_len += 1
            if head.next is None:
                tail_origin = head
                head.next = head_origin
                break
            head = head.next

        if k >= ll_len:
            k = k % ll_len

        new_head = head_origin
        new_tail = tail_origin
        for _ in range(ll_len - k):
            new_head = new_head.next
            new_tail = new_tail.next

        new_tail.next = None

        return new_head
