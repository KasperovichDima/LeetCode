class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        acc_lst = [0]*len(nums)
        right = len(nums) - 1
        acc_left = acc_right = left = 0

        while left < len(nums):
            if left >= right:
                if acc_lst[right - 1] == acc_lst[right + 1]:
                    return right
                if acc_lst[left - 1] == acc_lst[left + 1]:
                    return left
            acc_left += nums[left]
            acc_lst[left] = acc_left
            acc_right += nums[right]
            acc_lst[right] = acc_right
            left += 1
            right -= 1

        return -1





s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([1,2,3]))