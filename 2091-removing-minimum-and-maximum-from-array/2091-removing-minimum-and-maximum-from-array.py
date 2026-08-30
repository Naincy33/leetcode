class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # min_index ko left aur max_index ko right side maan lete hain
        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # 1. Dono front se
        front = right + 1

        # 2. Dono back se
        back = n - left

        # 3. Ek front se, ek back se
        both = (left + 1) + (n - right)

        return min(front, back, both)