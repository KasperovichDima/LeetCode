# class Solution:
#     def trap(self, height: list[int]) -> int:
#         left = result = 0
        
#         while left < len(height) - 1:
#             if not left:
#                 left += 1
#                 continue
#             right = left + 1
#             if height[right] >= height[left]:
#                 left += 1
#                 continue

#             # right wall found
#             ...  # here is the main code to impl
#             left = right



#         return result


class Solution:
    def trap(self, height: list[int]) -> int:
        left_ind = right_ind = result = occupied = 0
        gap_found = False

        for i in range(len(height)):
            if height[i] > height[left_ind]:
                # main logic
                ... # upd res and switch left
            elif not height[i]:
                gap_found = True
            elif height: # not 0 but lower than left
                ... # upd right and occupied

          