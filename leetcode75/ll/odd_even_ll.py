
class ListNode:
    def __init__(self, val: int=0, next: ListNode|None=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        odd = odd_head = head
        even = even_head = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return odd_head
    

# My original one

# class Solution:
#     def oddEvenList(self, head: ListNode | None) -> ListNode | None:
#         even_head = last_even = ListNode()
#         odd_head = last_odd = ListNode()
        
#         n = 1

#         while head:
#             node_to_attach = head

#             if n % 2:
#                 last_odd.next = node_to_attach
#                 last_odd = node_to_attach
#             else:
#                 last_even.next = node_to_attach
#                 last_even = node_to_attach

#             head = head.next
#             n += 1

#         if odd_head.next:
#             last_odd.next = even_head.next

#         last_even.next = None

#         return odd_head.next
