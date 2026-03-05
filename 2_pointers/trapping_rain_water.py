class Solution:
    def trap(self, height: list[int]) -> int:
        left = res = 0
        right = len(height) - 1
        top_left = top_right = 0
        while left <= right:
            if top_right < top_left:
                if height[right] < top_right:
                    res += top_right - height[right]
                else:
                    top_right = height[right]
                right -= 1
            else:
                if height[left] < top_left:
                    res += top_left - height[left]
                else:
                    top_left = height[left]
                left += 1

        return res

s = Solution()

# The Standard Mix
assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

# The "Descending Slope" (Your Nemesis)
assert s.trap([10, 0, 9, 0, 8]) == 17

# The "Staircase" (Should be Zero)
assert s.trap([1, 2, 3, 4, 5]) == 0
assert s.trap([5, 4, 3, 2, 1]) == 0

# The "Twin Peaks" (Deep Valley)
assert s.trap([5, 0, 0, 0, 5]) == 15

# The "Middle Peak"
assert s.trap([1, 2, 10, 2, 1]) == 0

# The "Bowl"
assert s.trap([3, 1, 2, 1, 4]) == 5

# Empty/Single cases
assert s.trap([5]) == 0
assert s.trap([5, 2]) == 0

# Large Gaps
assert s.trap([4, 2, 0, 3, 2, 5]) == 9

assert s.trap([5,5,1,7,1,1,5,2,7,6]) == 23