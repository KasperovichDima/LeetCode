

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_right: list[int] = [1] # prod of void is 1. Don't ask. just 1.
        for i in range(len(nums) - 1): # iterate left -> right
            left_right.append(nums[i] * left_right[i]) # some magic. cannot explain. just do it.

        s = 1 # another type of prod of void. also 1. don't ask. just 1.
        for i in range(len(nums) - 1, -1, -1): # iterate right -> left
            left_right[i] *= s # updating prev result by mult on accumulated right->left
            s *= nums[i] # updating accumulated result somehow. cannot explain. just do it.

        return left_right # abracadabra. done.


s = Solution()
s.productExceptSelf([1,2,3,4])