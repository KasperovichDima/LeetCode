# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        
        fake_left = ListNode()
        left = fake_left
        fake_right = ListNode()
        right = fake_right

        cur = head

        while cur is not None:
            if cur.val < x:
                left.next = cur
                left = cur
            else:
                right.next = cur
                right = cur

            cur = cur.next

        left.next = fake_right.next
        right.next = None

        return fake_left.next