class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        res = zeros = left = right = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                left += 1
                zeros -= nums[left]
            else:
                res = max(res, right - left)
            right += 1

        return res



        # zeros = i = 0
        # while zeros < k and i < len(nums):
        #     if nums[i] == 0:
        #         zeros += 1
        #     i += 1

        # max_res = this_res = i
       

        # return max_res
    

s = Solution()
assert s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2) == 6
