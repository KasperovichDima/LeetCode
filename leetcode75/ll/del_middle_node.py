
class ListNode:
    def __init__(self, val:int=0, next:ListNode|None=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        d = l = ListNode(next=head)
        r = head

        while r and r.next:
            l = l.next
            r = r.next.next

        l.next = l.next.next

        return d.next
