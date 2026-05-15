"""
🧩 QUESTION:
-------------
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of another word.

Example:
---------
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]

Explanation:
-------------
The substring starting at index 0 is "cba" → an anagram of "abc".
The substring starting at index 6 is "bac" → an anagram of "abc".

Constraints:
------------
1 <= len(s), len(p) <= 3 * 10^4
s and p consist of lowercase English letters only.
"""

# 🧠 APPROACH: Sliding Window + Frequency Count
# --------------------------------------------------
# 1️⃣ Count frequency of each char in 'p'  → count_p
# 2️⃣ Use a sliding window of size len(p) in 's'
# 3️⃣ Maintain a running count for current window → count_s
# 4️⃣ Whenever both frequency maps match → record start index
#
# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(1) (since 26 lowercase letters only)

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_p, len_s = len(p), len(s)
        if len_p > len_s:
            return []

        # Frequency count for p and for first window in s
        count_p = Counter(p)
        count_s = Counter(s[:len_p])

        result = []

        # Check first window
        if count_p == count_s:
            result.append(0)

        # Slide window across s
        for i in range(len_p, len_s):
            # Add new character on right
            count_s[s[i]] += 1

            # Remove character that moves out from left
            count_s[s[i - len_p]] -= 1

            # Clean up zero counts (optional optimization)
            if count_s[s[i - len_p]] == 0:
                del count_s[s[i - len_p]]

            # Compare counts
            if count_p == count_s:
                result.append(i - len_p + 1)

        return result


# 🧪 TEST CASE
s = "cbaebabacd"
p = "abc"
print("Anagram start indices:", Solution().findAnagrams(s, p))
