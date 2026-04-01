"""
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[str] = []
        result: list[str] = []
        digit = ''

        for i, c in enumerate(s):
            if c.isdigit():
                digit += c
            elif c == '[':
                for _ in range(i, len(s)):
                    if s[_] == '[':
                        stack.append(s[_])
                    elif s[_] == ']':
                        stack.pop()
                        if not stack:
                            return int(digit) * self.decodeString(s[i + 1: _])
            else:
                result.append(c)

        return ''.join(result)
    

s = Solution()
print(s.decodeString(s = "3[a]2[bc]"))
