from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            best = nums[i] + nums[left] + nums[right]
            best_diff = abs(best - target)

            while left != right:
                current = nums[i] + nums[left] + nums[right]
                current_dif = abs(current - target)
                if current_dif < best_diff:
                    best = current
                    best_diff = current_dif
                if current < target:
                    left += 1
                else:
                    right -= 1

        return best
    

s = Solution()

assert(s.threeSumClosest([-1,2,1,-4], 1)) == 2
# assert(s.threeSumClosest([0,0,0], 1)) == 0
