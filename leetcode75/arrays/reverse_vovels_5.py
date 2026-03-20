vovels = set('aeiouAEIOU')


class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        l = 0
        r = len(chars) - 1
        while l <= r:
            if chars[l] not in vovels:
                l += 1
            elif chars[r] not in vovels:
                r -= 1
            else:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

        return ''.join(chars)
    

s = Solution()
assert s.reverseVowels("IceCreAm") == "AceCreIm"
assert s.reverseVowels("leetcode") == "leotcede"

assert s.reverseVowels("HelloWorld") == "HolloWerld"
assert s.reverseVowels("Python") == "Python"
assert s.reverseVowels("AEIOU") == "UOIEA"
assert s.reverseVowels("aA") == "Aa"
assert s.reverseVowels("Programming") == "Prigrammong"
assert s.reverseVowels("OpenAI") == "IpAneO"
assert s.reverseVowels("ReverseVowels") == "RivArseVowels"
assert s.reverseVowels("TestCase") == "TastCese"
assert s.reverseVowels("beautiful") == "buetiaful"
assert s.reverseVowels("xyz") == "xyz"