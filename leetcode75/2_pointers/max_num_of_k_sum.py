class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = res = 0
        r = len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                r -= 1
                l += 1
                res += 1
            elif s > k:
                r -= 1
            else:
                l += 1

        return res
