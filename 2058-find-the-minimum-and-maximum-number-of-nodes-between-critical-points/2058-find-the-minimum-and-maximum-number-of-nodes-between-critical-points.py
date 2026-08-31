class Solution:
    def nodesBetweenCriticalPoints(self, head):
        critical = []
        
        prev = head
        curr = head.next
        index = 1
        
        while curr and curr.next:
            nxt = curr.next
            
            # Local maxima OR local minima
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                critical.append(index)
            
            prev = curr
            curr = nxt
            index += 1
        
        # Fewer than 2 critical points
        if len(critical) < 2:
            return [-1, -1]
        
        # Minimum distance
        minDistance = float('inf')
        
        for i in range(1, len(critical)):
            minDistance = min(
                minDistance,
                critical[i] - critical[i - 1]
            )
        
        # Maximum distance
        maxDistance = critical[-1] - critical[0]
        
        return [minDistance, maxDistance]