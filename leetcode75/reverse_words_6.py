class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
    

s = Solution()

assert s.reverseWords("the sky is blue") == "blue is sky the"