# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]



class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = 0
        while r < len(nums):
            if nums[r]:
                nums[w] = nums[r]
                w += 1
            r += 1
        for i in range(w, len(nums)):
            nums[i] = 0

nums = [0,1,0,3,12]
nums = [0]
s = Solution()
s.moveZeroes(nums)
print(nums)
