class Solution:
    def getSubarrayBeauty(self, nums, k, x):

        freq = [0] * 101

        ans = []

        i = 0

        for j in range(len(nums)):

            # add current element
            freq[nums[j] + 50] += 1

            # window complete
            if j - i + 1 == k:

                cnt = 0
                beauty = 0

                # check negatives from -50 to -1
                for num in range(-50, 0):

                    cnt += freq[num + 50]

                    if cnt >= x:
                        beauty = num
                        break

                ans.append(beauty)

                # remove left element
                freq[nums[i] + 50] -= 1
                i += 1

        return ans
# Time complexity: O(n * 50) where n is the length of the nums list and we check at most 50 negative numbers for each window
# Space complexity: O(1) since we are using a fixed-size frequency array of length 101
solution = Solution()
nums = [1, -1, -3, -2, 3]
k = 3
x = 2
print(solution.getSubarrayBeauty(nums, k, x))   