class BrutalSolution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        return [c + extraCandies >= m for c in candies]


s = BrutalSolution()
assert s.kidsWithCandies([2,3,5,1,3], 3) == [True, True, True, False, True]
assert s.kidsWithCandies([4,2,1,1,2], 1) == [True, False, False, False, False]
assert s.kidsWithCandies([12, 1, 12], 10) == [True, False, True]

# Все дети имеют одинаковое количество конфет
# Любое количество extraCandies сделает каждого "лидером"
assert s.kidsWithCandies([5, 5, 5], 2) == [True, True, True]

# Огромный разрыв: даже с добавкой никто не догонит лидера
assert s.kidsWithCandies([1, 20, 1], 5) == [False, True, False]

# Только один ребенок в списке
assert s.kidsWithCandies([10], 1) == [True]

# extraCandies равно 0 (проверяем, кто уже является лидером)
assert s.kidsWithCandies([2, 5, 3], 0) == [False, True, False]

# Лидеры делят первое место, и добавка позволяет другим к ним присоединиться
assert s.kidsWithCandies([10, 5, 10], 5) == [True, True, True]