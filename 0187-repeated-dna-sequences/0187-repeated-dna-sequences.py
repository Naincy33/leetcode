class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen=set()
        repeated= set()

        n=len(s)

        for i in range(n-10+1):
            sub=s[i:i+10]

            if sub in seen:
                repeated.add(sub)

            else:
                seen.add(sub)

        return list(repeated)



