class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            p = (l + r) // 2
            if nums[p] == target:
                return p

            if nums[l] <= nums[p]: # if left is ok (can contain just 1 element so use <=)
                if nums[l] <= target < nums[p]: # and target is on normal peace
                    r = p - 1 # excluding right peace
                else:
                    l = p + 1 # excluding left peace
            else: # right peace is ok
                if nums[p] <= target < nums[r]: # and target is on normal peace
                    l = p + 1 # excluding left peace
                else:
                    r = p - 1 # excluding right peace

        return -1


s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([1], 0) == -1


# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         l = 0
#         r = len(nums) - 1
#         while l <= r:
#             p = (l + r) // 2

#             if nums[p] == target:
#                 return p

#             if nums[l] <= nums[p]:
#                 if nums[l] <= target < nums[p]:
#                     r = p - 1
#                 else:
#                     l = p + 1
#             else:
#                 if nums[p] < target <= nums[r]:
#                     l = p + 1
#                 else:
#                     r = p - 1

#         return -1