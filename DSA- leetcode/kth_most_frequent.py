"""Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears once.
The top 2 frequent elements are 1 and 2.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Step 1: Count frequency manually using a dictionary
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        # Step 2: Sort dictionary items by frequency (descending order)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Pick top k elements (only the number, not its count)
        result = []
        for i in range(k):
            result.append(sorted_freq[i][0])

        return result
    
nums = [1, 1, 1, 2, 2, 3]
k = 2
obj = Solution()
print(obj.topKFrequent(nums, k))