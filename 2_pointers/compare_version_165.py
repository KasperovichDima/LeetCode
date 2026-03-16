class Solution1:
    def compareVersion(self, version1: str, version2: str) -> int:
        i1 = i2 = 0
        while i1 < len(version1) and i2 < len(version2):
            if version1[i1] == '0':
                i1 += 1
                continue
            if version2[i2] == '0':
                i2 += 1
                continue
            if version1[i1] == version2[i2] == '.':
                i1 += 1
                i2 += 1
                continue
            if int(version1[i1]) > int(version2[i2]):
                return 1
            elif int(version1[i1]) > int(version2[i2]):
                return -1
            i1 += 1
            i2 += 1
        
        return 0
    

class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        i1 = i2 = 0
        while i1 < len(version1) and i2 < len(version2):
            num1 = num2 = ''
            while i1 < len(version1) and i2 < len(version2) and version1[i1] != '.' and version2[i2] != '.':
                if version1[i1].isdigit():
                    if (num1 and version1[i1] == '0') or (version1[i1] != '0'):
                        num1 += version1[i1]
                if version1[i2].isdigit():
                    if (num2 and version2[i2] == '0') or (version2[i2] != '0'):
                        num2 += version2[i2]
                i1 += 1
                i2 += 1

            num1i = int(num1)
            num2i = int(num2)
            if num1i < num2i:
                return -1
            elif num1i > num2i:
                return -1
            i1 += 1
            i2 += 1

        return 0
    

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i1 = i2 = 0
        while i1 < len(version1) and i2 < len(version2):
            # finding num1
            i1c = i1
            while i1 < len(version1) and version1[i1] != '.':
                i1 += 1
            num1 = int(version1[i1c:i1])
            i1 += 1
            # finding num2
            i2c = i2
            while i2 < len(version2) and version2[i2] != '.':
                i2 += 1
            num2 = int(version2[i2c:i2])
            i2 += 1
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        if len(version1) == len(version2):
            return 0
        v, i, res = (version1, i1, 1) if len(version1) > len(version2) else (version2, i2, -1)
        for _ in range(i, len(v)):
            if v[_] != '.' and v[_] != '0':
                return res
        return 0

        
    

s = Solution()
assert s.compareVersion('1.2', '1.10') == -1
assert s.compareVersion('1.01', '1.001') == 0

assert s.compareVersion('1.0', '1.0.0') == 0
assert s.compareVersion('0.1', '1.1') == -1
assert s.compareVersion('1.0.1', '1') == 1
assert s.compareVersion('1.0.0.0', '1') == 0
assert s.compareVersion('1.0.0.1', '1') == 1
assert s.compareVersion('7.5.2.4', '7.5.3') == -1
assert s.compareVersion('1.01', '1.001.0') == 0
assert s.compareVersion('1.0.3', '1.0.3.0.0') == 0
assert s.compareVersion('00004.45.3', '4.46.3') == -1
assert s.compareVersion('4.46.3', '00004.45.3') == 1
assert s.compareVersion('3.10.2', '3.2.100') == 1
assert s.compareVersion('1.0.0.0.0.2', '1.0.0.0.0.10') == -1
assert s.compareVersion('10.0', '2.0') == 1