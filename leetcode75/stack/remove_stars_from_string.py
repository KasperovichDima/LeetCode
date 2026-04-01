class Solution:
    def removeStars(self, s: str) -> str:
        stack: list[str] = []
        for symb in s:
            if symb != '*':
                stack.append(symb)
            else:
                stack.pop()

        return ''.join(stack)
    

s = Solution()
print(s.removeStars(s = "leet**cod*e"))
print(s.removeStars(s = "erase*****"))