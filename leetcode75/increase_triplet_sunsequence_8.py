from collections import deque


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n < first:
                first = n
            elif n < second:
                second = n
            elif n > second:
                return True

        return False


class Solution2:
    def increasingTriplet(self, nums: list[int]) -> bool:
        d = deque(maxlen=2)
        