vowels = set('aeiou')

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        for i in range(k):
            if s[i] in vowels:
                res +=1

        this = res

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                this -= 1
            if s[i] in vowels:
                this += 1
            res = max(res, this)

        return res
    
s = Solution()
assert s.maxVowels(s = "abciiidef", k = 3) == 3
assert s.maxVowels(s = "aeiou", k = 2) == 2
assert s.maxVowels(s = "leetcode", k = 3) == 2
