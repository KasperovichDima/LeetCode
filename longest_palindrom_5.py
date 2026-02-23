class Solution:

    def longestPalindrome(self, s: str) -> str:
        best_left = best_right = 0
        
        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                    if (right - left) >= (best_right - best_left):
                        best_left = left
                        best_right = right
                    left -= 1
                    right += 1

        return s[best_left: best_right + 1]



s = Solution()
assert s.longestPalindrome("a") == 'a'
assert s.longestPalindrome("bb") == 'bb'
assert s.longestPalindrome("babad") == 'bab'
assert s.longestPalindrome("cbbd") == 'bb'
assert s.longestPalindrome("aab") == "aa"
assert s.longestPalindrome("baa") == "aa"
assert s.longestPalindrome("aaaaa") == "aaaaa"
assert s.longestPalindrome("baab") == "baab"
assert s.longestPalindrome("racecar") == "racecar"
