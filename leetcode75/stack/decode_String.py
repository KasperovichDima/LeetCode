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


import array


class Solution:
    def decodeString(self, s: str) -> str:
        stack_nums: array.array[int] = array.array('i')
        stack_chars: list[str] = []
        digit = 0
        string: str = ''

        for c in s:
            if c == '[':
                stack_chars.append(string)
                stack_nums.append(digit)
                string = ''
                digit = 0
            elif c == ']':
                symbols = stack_chars.pop()
                mltplr = stack_nums.pop()
                string = symbols + string * mltplr
            elif c.isdigit():
                digit = digit * 10 + int(c)
            else:
                string += c

        return string


s = Solution()
print(s.decodeString(s = "3[a]2[bc]"))
