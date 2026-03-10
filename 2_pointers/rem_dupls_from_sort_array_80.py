class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        for n in nums:
            if left < 2 or n != nums[left - 2]:
                nums[left] = n
                left += 1
        return left
    

s = Solution()



assert s.removeDuplicates([1,1,1,2,2,3]) == 5
assert s.removeDuplicates([0,0,1,1,1,1,2,3,3]) == 7

assert s.removeDuplicates([1,1,1]) == 2
assert s.removeDuplicates([1,1,1,1,1,1,1,1]) == 2
assert s.removeDuplicates([1,2,3]) == 3
assert s.removeDuplicates([1,1,2,2]) == 4
assert s.removeDuplicates([1,1,1,2,2,2,3,3,3]) == 6
assert s.removeDuplicates([1]) == 1
assert s.removeDuplicates([0,0,0,0,0]) == 2
