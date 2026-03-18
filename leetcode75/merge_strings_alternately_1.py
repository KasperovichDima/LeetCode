class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        for i in range(max(len(word1), len(word2))):
            if i <= len(word1) - 1:
                res += word1[i]
            if i <= len(word2) - 1:
                res += word2[i]
        return res
    

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        short, long = sorted((word1, word2), key=len)
        mixed_symbols: list[str] = []
        for i in range(len(short)):
            mixed_symbols.append(word1[i])
            mixed_symbols.append(word2[i])

        return ''.join(mixed_symbols) + long[len(short):]
    

s = Solution()


assert s.mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr"
assert s.mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs"
assert s.mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd"

assert s.mergeAlternately(word1 = "a", word2 = "z") == "az"
assert s.mergeAlternately(word1 = "abc", word2 = "z") == "azbc"
assert s.mergeAlternately(word1 = "a", word2 = "zyx") == "azyx"
assert s.mergeAlternately(word1 = "race", word2 = "car") == "rcaacre"
assert s.mergeAlternately(word1 = "longword", word2 = "s") == "lsongword"