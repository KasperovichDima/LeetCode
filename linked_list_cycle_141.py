# Definition for singly-linked list.
from typing import Any


class ListNode:
    def __init__(self, x: Any):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
    