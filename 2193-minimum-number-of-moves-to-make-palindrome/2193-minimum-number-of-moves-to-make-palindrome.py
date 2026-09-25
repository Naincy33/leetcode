class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)

        l = 0
        r = len(s) - 1
        moves = 0

        while l < r:

            if s[l] == s[r]:
                l += 1
                r -= 1
                continue

    
            k = r

            while k > l and s[k] != s[l]:
                k -= 1

            if k > l:
                
                while k < r:
                    s[k], s[k + 1] = s[k + 1], s[k]
                    k += 1
                    moves += 1

            else:
               
                k = l

                while k < r and s[k] != s[r]:
                    k += 1

                while k > l:
                    s[k], s[k - 1] = s[k - 1], s[k]
                    k -= 1
                    moves += 1

            l += 1
            r -= 1

        return moves