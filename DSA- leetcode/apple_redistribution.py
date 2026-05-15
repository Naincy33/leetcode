class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        
        capacity.sort(reverse=True)
        
        count = 0
        for cap in capacity:
            total_apples -= cap
            count += 1
            if total_apples <= 0:
                return count
        
        return count
obj = Solution()
print(obj.minimumBoxes([5,1,3,7,9],[4,8,1,4,2]))