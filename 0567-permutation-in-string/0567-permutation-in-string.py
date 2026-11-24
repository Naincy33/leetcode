class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # Count frequency of s1 and first window of s2
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        # Compare first window
        if freq1 == freq2:
            return True

        # Slide the window
        for i in range(len(s1), len(s2)):

            # Remove outgoing character
            freq2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            # Add incoming character
            freq2[ord(s2[i]) - ord('a')] += 1

            if freq1 == freq2:
                return True

        return False