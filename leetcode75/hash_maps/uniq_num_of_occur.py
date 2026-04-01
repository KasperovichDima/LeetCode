from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        c = Counter(arr)
        seen = set()
        for v in c.values():
            if v in seen:
                return False
            seen.add(v)
        return True
        