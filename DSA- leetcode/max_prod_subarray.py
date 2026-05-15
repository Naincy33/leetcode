class Solution:
    def maxProduct(self, nums):
        # Initialize the first element as base
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        print(f"i | num | max_prod | min_prod | ans")
        print("-" * 40)
        print(f"0 | {nums[0]:3} | {max_prod:8} | {min_prod:8} | {ans:3}")

        # Loop from index 1 to end
        for i in range(1, len(nums)):
            num = nums[i]

            # ⚡ If num is negative, swap max and min
            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            # Update max and min product ending at current index
            max_prod = max(num, num * max_prod)
            min_prod = min(num, num * min_prod)

            # Update global answer
            ans = max(ans, max_prod)

            # Print step-by-step changes
            print(f"{i} | {num:3} | {max_prod:8} | {min_prod:8} | {ans:3}")

        return ans


# 🔹 Test
nums = [2, 3, -2, 4, -1]
sol = Solution()
result = sol.maxProduct(nums)
print("\n✅ Final Maximum Product Subarray =", result)
