# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: ListNode|None=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        fast = head
        prev = None

        while fast and fast.next:
            this = head
            fast = fast.next.next
            head = head.next

            this.next = prev
            prev = this

        # now head is a middle point
        best = 0
        while prev:
            best = max(best, prev.val + head.val)
            head = head.next
            prev = prev.next
        return best