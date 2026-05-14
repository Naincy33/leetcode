class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        nums = [str(i) for i in range(1, n + 1)]

        # factorials store
        fact = [1] * n

        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        k -= 1

        ans = []

        for i in range(n, 0, -1):

            block_size = fact[i - 1]

            index = k // block_size

            ans.append(nums[index])

            nums.pop(index)

            k %= block_size

        return "".join(ans)
# Time complexity: O(n^2) due to the pop operation on the list
# Space complexity: O(n) for the nums list and the ans list         

solution = Solution()

n = 3
k = 3

print(solution.getPermutation(n, k))