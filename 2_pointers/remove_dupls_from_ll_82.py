class ListNode:
    def __init__(self, val: int = 0, next:ListNode|None=None):
        self.val = val
        self.next = next


# Constraints:

#     The number of nodes in the list is in the range [0, 300].
#     -100 <= Node.val <= 100
#     The list is guaranteed to be sorted in ascending order.



def get_head(nums: list[int]) -> ListNode|None:
    dummy = cur = ListNode()
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next



class Solution:
    def deleteDuplicates(self, head: ListNode|None) -> ListNode|None:
        ...

        
    

s = Solution()
cases: list[tuple[list[int], list[int]]] = [
    # ([1,1,2], [2]),
    # ([1,1,1,2,3], [2,3]),
    # ([1,1,1], []),
    ([1,2,3], [1,2,3]),
]

for nums, expected in cases:
    head = get_head(nums)
    result = s.deleteDuplicates(head)
    output: list[int] = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == expected, f"Expected {expected}, but got {output}"