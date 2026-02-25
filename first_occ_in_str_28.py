class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # +1 to check the last possible char in haystack
        for h_i in range(len(haystack) - len(needle) + 1):
            if haystack[h_i] == needle[0]:
                _ = h_i
                for char in needle:
                    if char == haystack[_]:
                        _ += 1
                    else:
                        break
                else:
                    return h_i

        return -1


s = Solution()
assert s.strStr("sadbutsad", "sad") == 0
assert s.strStr("leetcode", "leeto") == -1

assert s.strStr("hello", "ll") == 2
assert s.strStr("aaaaa", "bba") == -1
assert s.strStr("aaaaa", "aaa") == 0
assert s.strStr("mississippi", "issip") == 4
assert s.strStr("mississippi", "issi") == 1
assert s.strStr("abc", "c") == 2
assert s.strStr("abc", "abc") == 0
assert s.strStr("abc", "abcd") == -1
assert s.strStr("a", "a") == 0
assert s.strStr("a", "b") == -1