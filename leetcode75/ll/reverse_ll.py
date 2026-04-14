# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: ListNode|None=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        prev = None

        while head:
            this = head
            head = head.next
            this.next = prev
            prev = this
            
        return prev