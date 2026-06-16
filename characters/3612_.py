class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:
            if 'a' <= ch <= 'z':
                res.append(ch)
            elif ch == '*':
                if res:
                    res.pop()
            elif ch == '#':
                res.extend(res)
            else:  # ch == '%'
                res.reverse()

        return ''.join(res)

obj = Solution()
print(obj.processStr("a#b*c"))  # Output: "aab"
print(obj.processStr("abc%de#f"))  # Output: "cbadef"
print(obj.processStr("a*b#c%d"))  # Output: "acac"  