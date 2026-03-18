"""Recursion here works like
ABABABABAB
ABAB

ABABAB
ABAB

AB
ABABA

AB
AB
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short, long = sorted((str1, str2), key=len)
        if long + short != short + long:# simple trick to find if there is a solution
            return ''
        if len(short) == len(long):
            return short # exit from recursion
        return self.gcdOfStrings(long[len(short):], short)


s = Solution()
assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
assert s.gcdOfStrings("LEET", "CODE") == ""

assert s.gcdOfStrings("AAAAAA", "AAA") == "AAA"
assert s.gcdOfStrings("ABCABCABC", "ABCABC") == "ABC"
assert s.gcdOfStrings("ABABABAB", "ABAB") == "ABAB"
assert s.gcdOfStrings("XYZXYZ", "XYZ") == "XYZ"
assert s.gcdOfStrings("AAAA", "AA") == "AA"
assert s.gcdOfStrings("ABAB", "AB") == "AB"
assert s.gcdOfStrings("ABCDEF", "ABC") == ""
assert s.gcdOfStrings("A", "A") == "A"
assert s.gcdOfStrings("BBBBBB", "BB") == "BB"
assert s.gcdOfStrings("ABABAB", "AB") == "AB"

assert s.gcdOfStrings(
    "TAUXXTAUXXTAUXXTAUXXTAUXX",
    "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
) == "TAUXX"

assert s.gcdOfStrings(
    "CXTXNCXTXNCXTXNCXTXNCXTXN",
    "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"
) == "CXTXN"