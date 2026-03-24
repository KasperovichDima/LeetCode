# from collections import deque


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        Key idea - do not reduce window size - just move it right on fail.
        We just bring the best result through the time.
        """

        left = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1 # exhaust k unit instead of zero counter

            if k < 0:
                if nums[left] == 0: # if we leave zero behind
                    k += 1 # restore k unit
                left += 1 # move left edge right

        return len(nums) - left

    
        # z_indexes: deque[int] = deque(maxlen=k + 1)
        # res = 0
        # left = -1

        # for i, right in enumerate(nums):
        #     if not right:
        #         z_indexes.append(i)
        #     if len(z_indexes) > k:
        #         left = z_indexes.popleft()
        #     else:
        #         res = max(res, i - left)

        # return res
    

s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(s.longestOnes([0, 1, 1], k = 0))
print(s.longestOnes([1, 0, 1], k = 1))