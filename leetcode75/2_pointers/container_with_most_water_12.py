class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            min_wall = min(height[l], height[r])
            res = max(
                res,
                min_wall * (r - l)
            )
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))