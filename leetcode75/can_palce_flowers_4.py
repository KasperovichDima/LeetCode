class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        def is_a_good_plot(i: int) -> bool:
            return (
                (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            )

        i = 0
        while i < len(flowerbed):
            if flowerbed[i]:
                i += 1
            elif is_a_good_plot(i):
                n -= 1
                i += 1
            i += 1
            if n <= 0:
                return True
        
        return False


s = Solution()
assert s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)
assert not s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)

assert s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)
assert s.canPlaceFlowers(flowerbed = [0], n = 1)
assert s.canPlaceFlowers(flowerbed = [0,0,1,0,0], n = 2)
assert s.canPlaceFlowers(flowerbed = [0,0,0,0,0], n = 3)

assert not s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)
assert not s.canPlaceFlowers(flowerbed = [1,0,1,0,1], n = 1)
assert not s.canPlaceFlowers(flowerbed = [0,1,0], n = 2)
assert not s.canPlaceFlowers(flowerbed = [1], n = 1)
assert not s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 5)

# можно посадить
assert s.canPlaceFlowers(flowerbed = [0], n = 1)
assert s.canPlaceFlowers(flowerbed = [0,0], n = 1)
assert s.canPlaceFlowers(flowerbed = [0,0,0], n = 1)
assert s.canPlaceFlowers(flowerbed = [0,0,0,0], n = 2)
assert s.canPlaceFlowers(flowerbed = [0,0,0,0,0], n = 3)
assert s.canPlaceFlowers(flowerbed = [0,0,1,0,0], n = 2)
assert s.canPlaceFlowers(flowerbed = [0,0,0,1,0,0], n = 2)
assert s.canPlaceFlowers(flowerbed = [0,0,0,0,0,0,0], n = 4)
assert s.canPlaceFlowers(flowerbed = [1,0,0,0,0,0,1], n = 2)

# нельзя посадить
assert not s.canPlaceFlowers(flowerbed = [1], n = 1)
assert not s.canPlaceFlowers(flowerbed = [1,0], n = 1)
assert not s.canPlaceFlowers(flowerbed = [0,1], n = 1)
assert not s.canPlaceFlowers(flowerbed = [1,0,1], n = 1)
assert not s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)
assert not s.canPlaceFlowers(flowerbed = [1,0,1,0,1], n = 1)
assert not s.canPlaceFlowers(flowerbed = [0,1,0], n = 2)
assert not s.canPlaceFlowers(flowerbed = [1,0,1,0,1,0,1], n = 2)
assert not s.canPlaceFlowers(flowerbed = [1,1,1,0,0,1], n = 1)
assert not s.canPlaceFlowers(flowerbed = [1,0,0,1,0,0,1], n = 3)


# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


#[0]
#[1]
#[0,1,0,0,1,0,0,1]