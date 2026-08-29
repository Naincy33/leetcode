class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        # Sort by value
        arr.sort()

        start = 0

        while start < n:
            end = start

            # Find the connected group
            while (
                end + 1 < n
                and arr[end + 1][0] - arr[end][0] <= limit
            ):
                end += 1

            # Get original indices of this group
            indices = [arr[i][1] for i in range(start, end + 1)]

            # Sort indices
            indices.sort()

            # Assign sorted values to sorted indices
            for i, index in enumerate(indices):
                nums[index] = arr[start + i][0]

            start = end + 1

        return nums