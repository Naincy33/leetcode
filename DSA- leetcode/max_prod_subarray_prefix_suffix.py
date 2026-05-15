class Solution:
    def maxProduct(self, nums):
        # Edge case: empty list
        if not nums:
            return 0

        prefix = 1
        suffix = 1
        ans = nums[0]
        n = len(nums)

        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]

            # Update max product seen so far
            ans = max(ans, prefix, suffix)

            # Reset product if 0 appears (can't extend subarray through zero)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

        return ans


# ---------- 🌟 Test / Object Creation ----------
if __name__ == "__main__":
    obj = Solution()

    nums_list = [
        [2, 3, -2, 4],        # ✅ Expected 6
        [2, 3, -2, 4, -1],    # ✅ Expected 48
        [-2, 0, -1],          # ✅ Expected 0
        [0, -3, 1, -2],       # ✅ Expected 6
        [-2, 3, -4],          # ✅ Expected 24
        [0, 0, 0],            # ✅ Expected 0
    ]

    for nums in nums_list:
        result = obj.maxProduct(nums)
        print(f"{nums} → Maximum Product Subarray = {result}")
