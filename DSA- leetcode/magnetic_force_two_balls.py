class Solution:
    def canPlace(self, pos, m, mid):
        count = 1         # first ball at pos[0]
        last = pos[0]

        for i in range(1, len(pos)):
            if pos[i] - last >= mid:
                count += 1
                last = pos[i]
            if count == m:
                return True

        return False

    def maxDistance(self, position, m):
        position.sort()

        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if self.canPlace(position, m, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
obj = Solution()
print(obj.maxDistance([1, 2, 8, 12, 20], 3))
