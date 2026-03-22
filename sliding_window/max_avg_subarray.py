class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = this_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            this_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, this_sum)

        return max_sum / k








class Solution1:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        max_sum = this_sum = sum(nums[:k])
        l = 1
        r = k

        while r < len(nums):
            this_sum += nums[r]
            this_sum -= nums[l - 1]

            max_sum = max(max_sum, this_sum)

            l += 1
            r += 1

        return max_sum / k

s = Solution()

# Case 1: Standard Example
# (12 - 5 - 6 + 50) = 51 / 4 = 12.75
assert s.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75

# Case 2: Single element, k=1
assert s.findMaxAverage([5], 1) == 5.0

# Case 3: All Negatives (The "Max Initializer" Trap)
# Windows: [-1,-12] sum=-13, [-12,-5] sum=-17, [-5,-6] sum=-11...
# Max sum is -11, so -11/2 = -5.5
assert s.findMaxAverage([-1, -12, -5, -6, -50, -3], 2) == -5.5

# Case 4: k equals array length
# (1 + 2 + 3) / 3 = 2.0
assert s.findMaxAverage([1, 2, 3], 3) == 2.0

# Case 5: Large values with smaller k
# Max is 1000/1 = 1000.0
assert s.findMaxAverage([1000, -500, 1000, -500], 1) == 1000.0

# Case 6: Window at the very end is the maximum
# [1, 1, 1, 10, 10], k=2 -> (10+10)/2 = 10.0
assert s.findMaxAverage([1, 1, 1, 10, 10], 2) == 10.0