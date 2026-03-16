class Solution:
    """"""
    def searchInsert(self, nums: list[int], target: int) -> int:
        # put pointers on the borders
        l = 0
        r = len(nums) - 1
        # we r looking for exact 1 postion to insert
        # so main condition is pointers meetup
        while l <= r: # to check even 1 elelent cases
            p = (l + r) // 2 # pivot is always middle between l and r
            if target > nums[p]:
                l = p + 1
            else:
                r = p - 1
        # l is the position where we have to insert
        return l 


s = Solution()
assert s.searchInsert([1,3,5,6], 5) == 2
assert s.searchInsert([1,3,5,6], 2) == 1
assert s.searchInsert([1,3,5,6], 7) == 4

# Target is smaller than any element (insert at the beginning)
assert s.searchInsert([1, 3, 5, 6], 0) == 0

# Target is larger than any element (insert at the end)
assert s.searchInsert([1, 3, 5, 6], 10) == 4

# Target matches the very first element
assert s.searchInsert([1, 3, 5, 6], 1) == 0

# Target matches the very last element
assert s.searchInsert([1, 3, 5, 6], 6) == 3

# Single element, target matches
assert s.searchInsert([5], 5) == 0

# Single element, target is smaller
assert s.searchInsert([5], 2) == 0

# Single element, target is larger
assert s.searchInsert([5], 10) == 1

# Target falls in a large gap
assert s.searchInsert([1, 10, 20, 30], 15) == 2

# Standard middle insertion
assert s.searchInsert([1, 3, 5, 7, 9], 4) == 2

# Handling duplicates (usually returns the first occurrence)
assert s.searchInsert([1, 3, 3, 3, 5], 3) == 1