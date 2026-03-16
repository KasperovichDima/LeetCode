

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            p = (l + r) // 2
            if nums[p] == target:
                return p

            if nums[p] > target:
                if target:


            else: # nums[p] < target
                ...
        return -1


s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([1], 0) == -1