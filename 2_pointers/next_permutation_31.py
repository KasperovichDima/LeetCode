class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lgth = len(nums) - 1
        for i in range(lgth, 0, -1):
            pivot = i - 1
            if nums[i] > nums[pivot]:
                i = lgth
                while nums[i] <= nums[pivot]:
                    i -= 1
                nums[i], nums[pivot] = nums[pivot], nums[i]
                nums[pivot + 1:] = reversed(nums[pivot + 1:])
                return
        nums.reverse()


s = Solution()
cases: tuple[tuple[list[int], list[int]], ...] = (
    # обычный простой случай
    ([1,2,3], [1,3,2]),
    # уже самая большая перестановка → переворот
    ([3,2,1], [1,2,3]),
    # средняя перестановка
    ([1,3,2], [2,1,3]),
    # с повторяющимися элементами
    ([1,1,5], [1,5,1]),
    ([1,5,1], [5,1,1]),
    # длинный массив
    ([1,2,3,6,5,4], [1,2,4,3,5,6]),
    # один элемент
    ([1], [1]),
    # два элемента, простое увеличение
    ([1,2], [2,1]),
    # два элемента, максимальный → переворот
    ([2,1], [1,2]),
)
for input, output in cases:
    s.nextPermutation(input)
    assert input == output, f'expected {output}, got {input}'
