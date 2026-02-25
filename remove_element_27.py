class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
        return left

            

s = Solution()

assert s.removeElement([3,2,2,3], 3) == 2
assert s.removeElement([0,1,2,2,3,0,4,2], 2) == 5
assert s.removeElement([3,2,2,3], 3) == 2
assert s.removeElement([0,1,2,2,3,0,4,2], 2) == 5
assert s.removeElement([1,2,3,4], 2) == 3
assert s.removeElement([0,0,0], 0) == 0
assert s.removeElement([1,2,3], 4) == 3
assert s.removeElement([1,2,0,2,3,2], 2) == 3
assert s.removeElement([2,2,2,2], 2) == 0
assert s.removeElement([2,1,2,3,2], 2) == 2
assert s.removeElement([1,3,2], 2) == 2
assert s.removeElement([], 0) == 0
assert s.removeElement([1], 1) == 0
assert s.removeElement([4,2,2,3,1,2,5], 2) == 4
assert s.removeElement([4,5], 4) == 1