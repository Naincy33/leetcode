""""Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
You must solve it in O(log (m+n)) time."""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2       # partition in nums1
            j = half - i                  # partition in nums2

            # -----------------------------
            # Safe boundary checking nums1
            # -----------------------------
            if i == 0:
                Aleft = float('-inf')
            else:
                Aleft = nums1[i - 1]

            if i == m:
                Aright = float('inf')
            else:
                Aright = nums1[i]

            # -----------------------------
            # Safe boundary checking nums2
            # -----------------------------
            if j == 0:
                Bleft = float('-inf')
            else:
                Bleft = nums2[j - 1]

            if j == n:
                Bright = float('inf')
            else:
                Bright = nums2[j]

            # --------------------------------------
            # Check if partitions are correct
            # --------------------------------------
            if Aleft <= Bright and Bleft <= Aright:
                # Found perfect partition
                if total % 2 == 1:
                    return max(Aleft, Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            # Move search window
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1
obj = Solution()

nums1 = [1, 3]
nums2 = [2]

result = obj.findMedianSortedArrays(nums1, nums2)
print(result)   # Output: 2
