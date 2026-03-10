

# from collections import Counter


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = i = 0
        right = len(nums) - 1

        while i <= right:

            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

        # c = Counter(nums)
        # nums.clear()
        # nums.extend([0] * c.get(0, 0))
        # nums.extend([1] * c.get(1, 0))
        # nums.extend([2] * c.get(2, 0))








s = Solution()

initial = [1, 0]
s.sortColors(initial)
assert initial == [0, 1]

initial = [2,0,2,1,1,0]
s.sortColors(initial)
assert initial == [0,0,1,1,2,2]

initial = [2,0,1]
s.sortColors(initial)
assert initial == [0,1,2]

# Case 3: все 0
initial = [0,0,0]
s.sortColors(initial)
assert initial == [0,0,0]

# Case 4: все 1
initial = [1,1,1]
s.sortColors(initial)
assert initial == [1,1,1]

# Case 5: все 2
initial = [2,2,2]
s.sortColors(initial)
assert initial == [2,2,2]

# Case 6: чередование 0,1,2
initial = [0,2,1,0,2,1]
s.sortColors(initial)
assert initial == [0,0,1,1,2,2]

# Case 7: один элемент
initial = [1]
s.sortColors(initial)
assert initial == [1]

# Case 8: два элемента
initial = [2,0]
s.sortColors(initial)
assert initial == [0,2]

initial = [2,2,0,0]
s.sortColors(initial)
assert initial == [0,0,2,2]

initial = [2,2,1,0,1,0]
s.sortColors(initial)
assert initial == [0,0,1,1,2,2]

initial = [2,0,2,0,1,1]
s.sortColors(initial)
assert initial == [0,0,1,1,2,2]

initial = [1,2,0]
s.sortColors(initial)
assert initial == [0,1,2]