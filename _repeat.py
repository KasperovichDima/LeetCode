class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            p = (l + r) // 2

            if nums[p] == target:
                return p

            if nums[l] <= nums[p]:
                if nums[l] <= target < nums[p]:
                    r = p - 1
                else:
                    l = p + 1
            else:
                if nums[p] < target <= nums[r]:
                    l = p + 1
                else:
                    r = p - 1

        return -1