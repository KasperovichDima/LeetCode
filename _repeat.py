class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]
        for i in range(len(nums) - 1):
            res.append(nums[i] * res[i])
        acc = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= acc
            acc *= nums[i]
        return res
    
s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))