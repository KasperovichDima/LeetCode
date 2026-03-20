class Solution:
    def compress(self, chars: list[str]) -> int:
        
        this = read = write = 0
        while read < len(chars):
            chars[write] = chars[this]
            while read < len(chars) and chars[this] == chars[read]:
                read += 1
            if (segm_len := read - this) > 1:
                for c in str(segm_len):
                    write += 1
                    chars[write] = c

            this = read
            write += 1

        return write
    

s = Solution()
assert s.compress(["a","a","b","b","c","c","c"]) == 6
assert s.compress(["a","a","a","a","a","a","a","a","a","a","a","a"]) == 3