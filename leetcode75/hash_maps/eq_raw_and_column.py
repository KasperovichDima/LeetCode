from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        hashes = Counter(tuple(r) for r in grid)
        res = 0
        for i in range(len(grid)):
            column = tuple(raw[i] for raw in grid)
            if column in hashes:
                res += hashes[column]

        return res
    

s = Solution()
assert s.equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]) == 1
assert s.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3