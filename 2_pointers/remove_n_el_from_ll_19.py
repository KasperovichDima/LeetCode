# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: ListNode|None=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode|None, n: int) -> ListNode|None:
        dummy = ListNode(0, head)
        
        left = right = dummy
        for _ in range(n):
            right = right.next

        while right.next is not None:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next