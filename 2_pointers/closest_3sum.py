from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = nums[0] + nums[1] + nums[2]
        best_diff = abs(target - best)

        for i in range(len(nums) - 2):
            if nums[i] > target > 0:
                return best
            left = i + 1
            right = len(nums) - 1

            while left != right:
                if (current := nums[i] + nums[left] + nums[right]) == target:
                    return current
                current_dif = abs(target - current)
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
assert(s.threeSumClosest([0,0,0], 1)) == 0
assert(s.threeSumClosest([-10, 1, 2, 3, 4, 5], 5)) == 6
assert(s.threeSumClosest([0, 1, 1, 10], 100)) == 12
assert(s.threeSumClosest([-10, -1, 0, 1], -100)) == -11
assert(s.threeSumClosest([-10, -5, 0, 5, 10], -2)) == 0
assert(s.threeSumClosest([-5, -4, -3, -2, -1], -10)) == -10
assert(s.threeSumClosest([-10, 0, 1, 10, 11], -10)) == -9
assert(s.threeSumClosest([-100, -98, -96, -94, 1, 2, 3], 0)) == 6
assert(s.threeSumClosest([-10, -5, -2, 1, 2], -6)) == -6
assert(s.threeSumClosest([-5, 1, 2, 10], 3)) == 6
assert(s.threeSumClosest([-10, -1, 2, 9, 20], 8)) == 9
assert(s.threeSumClosest([-5, 1, 2, 10], 3)) == 6
assert(s.threeSumClosest([0,3,97,102,200], 300)) == 300
