class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i//2] + (i%2)
        return result
    
obj= Solution()
print(obj.countBits(33))