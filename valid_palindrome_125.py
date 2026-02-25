class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
            
s = Solution()
assert s.isPalindrome('A man, a plan, a canal: Panama')
assert not s.isPalindrome('race a car')
assert s.isPalindrome(' ')

assert not s.isPalindrome("0P")
assert s.isPalindrome("aa")
assert s.isPalindrome("ab_a")
assert s.isPalindrome("Madam")
assert s.isPalindrome("No lemon, no melon")
assert s.isPalindrome("Was it a car or a cat I saw?")
assert s.isPalindrome("!@#")
assert not s.isPalindrome("1a2")
assert s.isPalindrome("1a1")