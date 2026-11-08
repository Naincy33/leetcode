class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        freq = {}

        # Step 1: Count frequency of each element
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        result = []

        # Step 2: Add elements according to arr2 order
        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]

        # Step 3: Add remaining elements in sorted order
        for num in sorted(freq.keys()):
            result.extend([num] * freq[num])

        return result