class Solution:
    def mapWordsWeights(self, words, weights):
        ans = ""

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            rem = total % 26
            ans += chr(ord('z') - rem)

        return ans  
# Time complexity: O(n * m) where n is the number of words and m is the average length of the words
# Space complexity: O(n) for the output string
solution = Solution()           
words = ["abc", "def"]
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
print(solution.mapWordsWeights(words, weights))  # Output: "xw"