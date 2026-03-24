class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        acc = 0
        max_alt = acc

        for g in gain:
            acc += g
            if acc > max_alt:
                max_alt = acc

        return max_alt
    

s = Solution()
print(s.largestAltitude([-5,1,5,0,-7]))
print(s.largestAltitude([-4,-3,-2,-1,4,3,2]))