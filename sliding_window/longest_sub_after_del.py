class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        units = 1
        left = 0
        for n in nums:
            if n == 0:
                units -= 1
            if units < 0:
                if nums[left] == 0:
                    units += 1
                left += 1

        return len(nums) - left - 1 # -1 to simulate element removal
    
s = Solution()
print(s.longestSubarray([1,1,0,1]))
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(s.longestSubarray([1,1,1]))