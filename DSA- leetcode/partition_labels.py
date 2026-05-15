class Solution(object):
    def partitionLabels(self, s):
        last = {}

        # Step 1: last occurrence of each char
        for i, ch in enumerate(s):
            last[ch] = i

        res = []
        start = 0
        end = 0

        # Step 2: greedy partition
        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res
obj= Solution()
print(obj.partitionLabels("ababcbacadefegdehijhklij"))