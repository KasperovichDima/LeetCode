class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        best = 0
        while left < right:
            current = min(height[right], height[left]) * (right - left)
            best = max(best, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best


s = Solution()
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert s.maxArea([1,1]) == 1