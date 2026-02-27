class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result: list[list[int]] = []

        for i in range(len(nums) - 2):  # right pointer is looking at last one
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:  # skipping duplicates of pivot
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                combo_sum = nums[i] + nums[left] + nums[right]
                if combo_sum > 0:
                    right -= 1
                elif combo_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result

                
s = Solution()
assert s.threeSum([0, 0, 0]) == [[0,0,0]]
assert s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]

# все элементы одинаковые
assert s.threeSum([0, 0, 0, 0]) == [[0,0,0]]

# несколько повторов и отрицательных
assert s.threeSum([-2,0,1,1,2]) == [[-2,0,2],[-2,1,1]]

# пустой результат
assert s.threeSum([1,2,-2,-1]) == []

# маленький массив
assert s.threeSum([0,1,-1]) == [[-1,0,1]]

# больше повторов
assert s.threeSum([-1,-1,-1,2,2,0,0]) == [[-1,-1,2],[-1,0,1],[0,0,0]]  # если 1 добавлен для тройки с 0
