class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_ptr = 0
        right_ptr = bottom_len =len(height) - 1

        min_side = min(height[left_ptr], height[right_ptr])
        best = min_side * bottom_len

        while left_ptr < right_ptr:
            if min_side == height[left_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
            bottom_len = right_ptr - left_ptr
            min_side = min(height[left_ptr], height[right_ptr])
            new_res = min_side * bottom_len
            best = max(best, new_res)

        return best

s = Solution()
assert s.max_area([1,8,6,2,5,4,8,3,7]) == 49
assert s.max_area([1,1]) == 1
