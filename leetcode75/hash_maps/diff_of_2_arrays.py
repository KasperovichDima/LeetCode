class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        shared = set(nums1) & set(nums2)
        res = []
        for nums in nums1, nums2:
            res.append([])
            available = set(nums)
            for n in nums:
                if n in available and n not in shared:
                    res[-1].append(n)
                    available.remove(n)

        return res