class Solution:
    def sumGame(self, num):
        n = len(num)
        
        sumL = sumR = 0
        cntL = cntR = 0
        
        for i in range(n // 2):
            if num[i] == '?':
                cntL += 1
            else:
                sumL += int(num[i])
        
        for i in range(n // 2, n):
            if num[i] == '?':
                cntR += 1
            else:
                sumR += int(num[i])
        
        # Odd number of '?' -> Alice wins
        if (cntL + cntR) % 2 == 1:
            return True
        
        # Bob wins only in this exact case
        return sumL - sumR != (cntR - cntL) * 9 // 2