from typing import Any


class ListNode:
    def __init__(self, x: Any):
        self.val = x
        self.next: None | ListNode

class Solution_1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        # Пиздуем сперва обеими указателями до конца.
        # Таким образом мы знаем длину общую первого связанного списка и длину второго связанного списка.
        len_a = len_b = 0
        origin_a = headA
        origin_b = headB
        while headA or headB:
            if headA:
                headA = headA.next
                len_a += 1
            if headB:
                headB = headB.next
                len_b += 1
        # Вычитаем разницу между ними и смещаем стартовые позиции обоих указателей.
        head_to_shift = origin_a if len_b > len_a else origin_b
        for _ in range(abs(len_a - len_b)):
            head_to_shift = head_to_shift.next

        # После этого опять же этими двумя указателями пиздуем до конца,
        # но на каждой итерации мы проверяем, являются ли они оба одним и тем же объектом в памяти.
        ...


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        origin_a = headA
        origin_b = headB

        while headA is not headB:
            headA = origin_b if headA is None else headA.next
            headB = origin_a if headB is None else headB.next
        return headA
        